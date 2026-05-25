def create_lookup_list(messages, labels) :
  lookup_list = []
  for message, label in zip(messages, labels):
    lookup_list.append({"message":message, "label":label})
  return lookup_list


def var_1(var_2, var_3) :
  var_4 = []
  for var_5, var_6 in zip(var_2, var_3):
    var_4.var_7({"message":var_5, "label":var_6})
  return var_4
