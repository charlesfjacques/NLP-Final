def load_file(filename):
    with open(filename, "r") as file:
        return file.readlines()
    
def load_cfg(filename):
    lines = load_file(filename)
    rules = []
    endpoints = {}
    grammar = {}
    for line in lines:
        line = line.strip()
        rule_name, rule_body = line.split("->")
        rule_name = rule_name.strip()
        rules.append(rule_name)
        items = [item.strip() for item in rule_body.split("|")]
        grammar[rule_name] = {
            "words": [],
            "rules": []
        }
        for item in items:
            if item[0] == "\"":
                endpoint = item[1:-1].lower()
                endpoints[endpoint] = rule_name
                grammar[rule_name]["words"].append(endpoint)
            elif item[0] == "@":
                load_file_into_cfg(item[1:], rule_name, rules, endpoints, grammar)
            else:
                grammar[rule_name]["rules"].append(item)
    return {
        "rules": rules,
        "endpoints": endpoints,
        "grammar": grammar
    }
def load_file_into_cfg(filename, rule_name, rules, endpoints, grammar):
    if(filename[0] == "\""):
        new_endpoints = load_file(filename[1:-1])
        new_endpoints = [word.strip().lower() for word in new_endpoints if len(word.strip()) > 0]

        for endpoint in new_endpoints:
            endpoints[endpoint] = rule_name
        grammar[rule_name]["words"] += new_endpoints
        return
    cfg = load_cfg(filename)
    for rule in cfg["rules"]:
        if rule not in grammar:
            rules.append(rule)
            grammar[rule] = cfg["grammar"][rule]
            for word in grammar[rule]["words"]:
                endpoints[word] = rule
    grammar[rule_name] = cfg["grammar"][cfg["rules"][0]]

def tokenize_string(string, cfg):
    words = [word.lower() for word in string.split()]
    tokens = []
    for i, word in enumerate(words):
        rule = cfg["endpoints"].get(word)
        if rule is None:
            return f"Unknown word \"{string.split()[i]}\"", None
        tokens.append((rule, word))
    return None, tokens

def apply_rule(rule, tokens, cfg):
    rule_applied = False
    for body in cfg["grammar"][rule]["rules"]:
        new_tokens = []
        body = body.split()
        i = 0
        while i < len(tokens):
            for di,item in enumerate(body):
                if i+di < len(tokens):
                    # matches
                    if tokens[i+di][0].lower() == item.lower():
                        continue
                    # sometimes a word can be in multiple "base" rules, and we might have
                    # labeled it as the wrong one
                    if type(tokens[i+di][1]) is str and tokens[i+di][1] in cfg["grammar"][item]["words"]:
                        tokens[i+di] = (item, tokens[i+di][1])
                        continue
                new_tokens.append(tokens[i])
                i += 1
                break
            else:
                rule_applied = True
                new_tokens.append((rule, tokens[i:i+len(body)]))
                i += len(body)
        tokens = new_tokens

    if rule_applied:
        return apply_rule(rule, tokens, cfg)[0], True
    return tokens, False
def parse_tokens(tokens, cfg):
    rules = list(cfg["rules"])
    rules.reverse()
    applied = True
    while applied:
        applied = False
        for rule in rules:
            tokens, rule_applied = apply_rule(rule, tokens, cfg)
            applied = applied or rule_applied
    return tokens

def parse_string(string, cfg):
    err, tokens = tokenize_string(string, cfg)
    if err is not None:
        return err, None
    ast = parse_tokens(tokens, cfg)
    print(ast)
    if ast[0][0] != cfg["rules"][0]:
        return "String is not a full sentence", None
    if len(ast) > 1:
        asts = ast[1:]
        return f"Unexpected token{"s" if len(asts) > 1 else ""} \"{" ".join(display_original(o) for o in asts)}\"", None 
    return None, ast[0]

def display_ast(ast):
    INDENT = "     "
    head = f"{ast[0]}:"
    while len(head)%len(INDENT) != 0:
        head += " "

    if type(ast[1]) is str:
        return f"{head}\"{ast[1]}\""
    
    children = [display_ast(child) for child in ast[1]]
    if len(children) == 1:
        return f"{head}{children[0]}"

    if len(children) == 2:
        head = f"{head}{f"\n{INDENT}".join(children[0].split("\n"))}"
        children = children[1:]
        
    indented = f"\n{INDENT}".join("\n".join(children).split("\n"))
    return f"{head}\n{INDENT}{indented}"
def display_original(ast):
    if type(ast[1]) is str:
        return ast[1]

    return " ".join([
        display_original(node)
        for node in ast[1]
    ])