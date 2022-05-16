from pprint import pp


class XMixin:
    def render(self, s):
        resp = super().render(s)
        return f"X-{resp}-X"


class A:
    def render(self, s):
        return f"A-{s}-A"


class B(A):
    def render(self, s):
        resp = super().render(s)
        return f"B-{resp}-B"


class XB(XMixin, B):
    pass


class BX(B, XMixin):
    pass


class C(B):
    def render(self, s):
        resp = super().render(s)
        return f"C-{resp}-C"


pp(XB.mro())  # Method Resolution Order
pp(BX.mro())

# o = XB()
# print(o.render("shalom"))
# o = BX()
# print(o.render("shalom"))
