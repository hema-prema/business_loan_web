from flask import Flask, render_template, request

app = Flask(__name__)

# Mocked balance sheet data for demonstration
balance_sheet_data = [
    {
        "year": 2022,
        "month": 12,
        "profitOrLoss": 15000,
        "assetsValue": 120000
    },
    {
        "year": 2022,
        "month": 11,
        "profitOrLoss": 12000,
        "assetsValue": 130000
    },
    {
        "year": 2022,
        "month": 10,
        "profitOrLoss": 8000,
        "assetsValue": 110000
    },
    {
        "year": 2022,
        "month": 9,
        "profitOrLoss": -5000,
        "assetsValue": 105000
    }
]


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        data = request.form

        business_name = data.get('businessName', '')
        year_established = data.get('yearEstablished', '')
        loan_amount = float(data.get('loanAmount', 0))
        accounting_provider = data.get('accountingProvider', '')

        last_12_months = balance_sheet_data[:12]
        made_profit = any(profit['profitOrLoss'] > 0 for profit in last_12_months)   #made profit in 12 months
        asset_values = [asset['assetsValue'] for asset in last_12_months]          #calculating avrage of asset values
        avg_asset_value = sum(asset_values) / len(asset_values)

        if made_profit:
            pre_assessment = 60
        elif avg_asset_value >= loan_amount:
            pre_assessment = 100
        else:
            pre_assessment = 20


        loan_application_result = {
            'businessName': business_name,
            'yearEstablished': year_established,
            'preAssessment': pre_assessment,
            'accounting_provider':accounting_provider
        }

        return render_template('index.html', result=loan_application_result, show_result=True)
    return render_template('index.html', show_result=False)


if __name__ == '__main__':
    app.run(debug=True)
