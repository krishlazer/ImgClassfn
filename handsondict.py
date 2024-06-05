def greatfntop(probefn):
    def greatinnerfn(proceedfn):
        print('How this function enhances the external function is a great thing to note.')
        print('Decorators truly is an excellent and poweful feature of Python.')
        return greatfntop(probefn)
    return greatinnerfn


def canfunc():
    print('Check if this function can really be enhanced by decorators' + checkitfn)


