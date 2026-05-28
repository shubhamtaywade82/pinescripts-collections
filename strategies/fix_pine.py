import re

with open('/home/nemesis/project/trading-workspace/pinescript/pinescripts-collections/strategies/test.pine', 'r') as f:
    lines = f.readlines()

vars_to_declare = [
    "stBullish", "stBearish",
    "kamaBullish", "kamaBearish",
    "ichiBullish", "ichiBearish", "cloudGreen",
    "trendLong", "trendShort",
    "macdBullish", "macdBearish", "macdBullCross", "macdBearCross",
    "srsiOversold", "srsiOverbought", "srsiBullish", "srsiBearish", "srsiExitLong", "srsiExitShort",
    "pzoBullish", "pzoBearish",
    "momLong", "momShort",
    "momEarlyLong", "momEarlyShort",
    "volSpike",
    "vzoBullish", "vzoBearish", "vzoStrong",
    "volLong", "volShort",
    "volEarlyLong", "volEarlyShort",
    "layer1FiresLong", "layer1FiresShort", "layer2FiresLong", "layer2FiresShort", "layer3FiresLong", "layer3FiresShort",
    "barsSinceLongTrigger", "barsSinceShortTrigger",
    "inLongWindow", "inShortWindow",
    "longLayersConfirm", "shortLayersConfirm",
    "fcfsLongValid", "fcfsShortValid",
    "longSignal", "shortSignal",
    "longTrailActive", "shortTrailActive",
    "vstopLongExit", "vstopShortExit",
    "chandelierLongExit", "chandelierShortExit",
    "fixedTPHitLong", "fixedTPHitShort", "fixedSLHitLong", "fixedSLHitShort",
    "exitLong", "exitShort",
    "inCooldown",
    "bgColor"
]

types_to_declare = {
    "exitReason": "string",
    "l1Color": "color",
    "l1Text": "string",
    "l2Color": "color",
    "l2Text": "string",
    "l3Color": "color",
    "l3Text": "string",
    "sigColor": "color",
    "sigText": "string",
    "posText": "string",
    "posColor": "color",
    "pnlColor": "color"
}

already_declared = set()

with open('/home/nemesis/project/trading-workspace/pinescript/pinescripts-collections/strategies/test.pine', 'w') as f:
    for line in lines:
        for var in vars_to_declare:
            if var not in already_declared:
                # Check if line starts with this variable (ignoring leading whitespace)
                match = re.match(r'^(\s*)' + var + r'\s*:=', line)
                if match:
                    line = line.replace(':=', '=', 1)
                    already_declared.add(var)
                    break
        
        for var, t in types_to_declare.items():
            if var not in already_declared:
                match = re.match(r'^(\s*)' + var + r'\s*:=', line)
                if match:
                    # e.g., '    l1Color :=' -> '    color l1Color ='
                    indent = match.group(1)
                    line = line.replace(indent + var + ' :=', indent + t + ' ' + var + ' =', 1)
                    if var == "exitReason":
                        # exitReason appears twice in different blocks, so we don't add to already_declared
                        pass
                    else:
                        already_declared.add(var)
                    break
        
        f.write(line)

print("Done")
