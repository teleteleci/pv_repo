a = [{"zm-dev17": {"xx": "valuex"}}, {"ws-dev17": {"yy": "valuey"}}]
for item in a:
    # print(item)
    for k, v in item.iteritems():
        # print("{} -> {}".format(k, v))
        for k, v in v.iteritems():
            print(v)

print("-------")
d = map(lambda x: filter(lambda y: y,  a),
        a)

print(d)
