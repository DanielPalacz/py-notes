
# Python Data Object Model
#  - when we can implement Magic methods and how we should do it?
#  - does this operation has 'explanatory power' (self-describing guidance)?
#  - is this operation unambiguous?
#  - is this operation unique?
#  - is this operation privileged?


# no additional modalities
# x = xs[idx]
# v = d[k]
# res = obj.a

# ???:
# res = f(123)

def f(data, *, mode):
    pass

# help(f)


class A:
    def __len__(self):
        return -1
