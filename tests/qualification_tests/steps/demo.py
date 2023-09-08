from behave import *

from sources.sub_module.util import A, B

use_step_matcher("re")


@when("first argument is 1")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.a = 1


@step("second argument is 2")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.b = 2


@given("addition method executed")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    a = A()
    context.result = a.add(context.a, context.b)


@then("result is 3")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.result == 3


@when("perform method")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    b = B()
    b.another_method()


@given("nothing")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("prints 'Something'")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert 'Something' in context.stdout_capture.getvalue()