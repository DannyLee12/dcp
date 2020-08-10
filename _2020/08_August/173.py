"""
This problem was asked by Stripe.

Write a function to flatten a nested dictionary. Namespace the keys with a
period.

For example, given the following dictionary:

{
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}

it should become:

{
    "key": 3,
    "foo.a": 5,
    "foo.bar.baz": 8
}

You can assume keys do not contain dots in them, i.e. no clobbering will occur.
"""


def flatten(d: dict) -> dict:
    """Flatten a dictionary, namespace with a period"""
    cd = {}
    for k, v in d.items():
        if isinstance(v, dict):
            flattened_subdict = flatten(v)
            for key, value in flattened_subdict.items():
                cd[f"{k}.{key}"] = value
        else:
            cd[k] = v

    return cd


if __name__ == '__main__':
    d = {"key": 3,"foo": {"a": 5, "bar": {"baz": 8}}}
    assert flatten(d) == {'key': 3, 'foo.a': 5, 'foo.bar.baz': 8}
