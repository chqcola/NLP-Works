def is_variable(pat):
    return pat.startswith('?') and all(s.isalpha() for s in pat[1:])
def is_pattern_segment(pattern):
    return pattern.startswith('?*') and all(a.isalpha() for a in pattern[2:])
fail = [True, None]
def pat_match_with_seg(pattern, saying):
    if not pattern or not saying: return []
    pat = pattern[0]
    if is_variable(pat):
        return [(pat, saying[0])] + pat_match_with_seg(pattern[1:], saying[1:])
    elif is_pattern_segment(pat):
        match, index = segment_match(pattern, saying)
        return [match] + pat_match_with_seg(pattern[1:], saying[index:])
    elif pat == saying[0]:
        return pat_match_with_seg(pattern[1:], saying[1:])
    else:
        return fail
def segment_match(pattern, saying):
    seg_pat, rest = pattern[0], pattern[1:]
    seg_pat = seg_pat.replace('?*', '?')

    if not rest: return (seg_pat, saying), len(saying)

    for i, token in enumerate(saying):
        if rest[0] == token and is_match(rest[1:], saying[(i + 1):]):
            return (seg_pat, saying[:i]), i
    return (seg_pat, saying), len(saying)
def is_match(rest, saying):
    if not rest and not saying:
        return True
    if not all(a.isalpha() for a in rest[0]):
        return True
    if rest[0] != saying[0]:
        return False
    return is_match(rest[1:], saying[1:])
def pat_to_dict(patterns):
    return {k: ' '.join(v) if isinstance(v, list) else v for k, v in patterns}
def subsitite(rule, parsed_rules):
    if not rule: return []
    return [parsed_rules.get(rule[i], rule[i])for i in range(len(rule))]
import random
choice = random.choice
def fit_rule(saying,rules):
    patterns = list(rules.keys())
    for pattern in patterns:
        pat = pattern.split()
        if not pat or not saying: continue
        for i in range(len(saying)):
            if is_variable(pat[i]):
                return pattern
            elif is_pattern_segment(pat[i]) and list(segment_match(pat,saying))[1] != len(saying):
                return pattern
            elif pat[i] != saying[i]: break
            else:continue
    return 'error'
rule_responses = {
    '?*x hello ?*y': ['How do you do', 'Please state your problem'],
    '?*x I want ?*y': ['what would it mean if you got ?y', 'Why do you want ?y', 'Suppose you got ?y soon'],
    '?*x if ?*y': ['Do you really think its likely that ?y', 'Do you wish that ?y', 'What do you think about ?y', 'Really-- if ?y'],
    '?*x no ?*y': ['why not?', 'You are being a negative', 'Are you saying \'No\' just to be negative?'],
    '?*x I was ?*y': ['Were you really', 'Perhaps I already knew you were ?y', 'Why do you tell me you were ?y now?'],
    '?*x I feel ?*y': ['Do you often feel ?y ?', 'What other feelings do you have?'],
}
def get_response(saying, response_rules):
    if fit_rule(saying.split(),response_rules) == 'error':
        return 'unfitness saying'
    return ' '.join(subsitite(choice(response_rules[fit_rule(saying.split(),response_rules)]).split(), pat_to_dict(pat_match_with_seg(fit_rule(saying.split(),response_rules).split(),saying.split()))))
print(get_response('Long Time ago I was fall in love with you',rule_responses))
