import clingo

clingo_files = ["FILL-LP-FILES"]


class Context:
    def id(self, x):
        return x

    def seq(self, x, y):
        return [x, y]

# ------------------------ Utils functions


def parse_model(m):
    ret = []
    for sym in m.symbols(shown=True):
        ret.append(str(sym))
    return ret


def assert_sat(models):
    assert (len(models) > 0), "Result is not SAT"


def assert_unsat(models):
    assert (len(models) == 0), "Result is not UNSAT, found models:{}".format(
        str(models))


def call_clingo(instance):
    ctl = clingo.Control(['0'])
    # FILL: Add propagators and applications
    for f in clingo_files:
        ctl.load(f)
    if instance[:-3] == ".lp":
        ctl.load(instance)
    else:
        ctl.add("base", [], instance)
    ctl.ground([("base", [])], context=Context())
    models = []
    ctl.solve(on_model=lambda m: models.append(parse_model(m)))
    return models


def check_fact(fact):
    models = call_clingo(":-not {}.".format(fact))
    assert (len(models) > 0), "Fact {} not in output".format(fact)


# ------------------------ Tests


def test():
    # Add tests here
    pass
