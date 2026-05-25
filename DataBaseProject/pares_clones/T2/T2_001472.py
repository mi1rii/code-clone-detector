def create_lookup_list(messages, schema) :
  lookup_list = []
  for message in messages:
    message_dict = {}
    for key, value in zip(schema, message):
        message_dict[key] = value
    lookup_list.append(message_dict)
  return lookup_list


def var_1(var_2, var_3) :
  var_4 = []
  for var_5 in var_2:
    var_6 = {}
    for var_7, var_8 in zip(var_3, var_5):
        var_6[var_7] = var_8
    var_4.var_9(var_6)
  return var_4
