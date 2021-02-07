from behave import given, when, then
import requests


@given(u'the number of page details')
def step_impl(context):
    context.url = "https://reqres.in/api/users"
    context.param = {
        "page": 2,
    }


@when(u'pass the page number in list user')
def step_impl(context):
    context.response = requests.get(context.url, context.param)


@then(u'get the user details')
def step_impl(context):
    print(context.response.json())
