import logging

import azure.functions as func

from prediction import make_prediction

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    tenure = req.params.get('tenure') #parameter tenure is what we need from user
    monthly = req.params.get('monthly') 
    techsupport = req.params.get('techsupport')

    prediction = make_prediction(
        tenure=tenure, #the parameters are the same as in prediction.py features list
        MonthlyCharges=monthly,
        TechSupport_yes=techsupport
    )

    if tenure and monthly and techsupport:
        return func.HttpResponse(f"The probability that this customer will churn is {prediction}.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a tenure, monthly, techsupport to get prediction.",
             status_code=200
        )