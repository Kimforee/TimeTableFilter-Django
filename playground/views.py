import pandas as pd
from django.shortcuts import render, redirect

def timetable(request):
    # Load the Excel sheet from Google Sheets
    sheet = 'BTECH 5 SEM'
    time_table_df = pd.read_excel('D:/Django/webtech/playground/templates/sheet.xlsx' )
    time_table_df.iloc[:, 0] = time_table_df.iloc[:, 0].ffill()
    time_table_df.fillna('No Class', inplace=True)
   
    # Convert the data to HTML table
    table_html = time_table_df.to_html(index=False)

    # Render the full time table HTML template
    return render(request, 'timetable.html', {'table_html': table_html})

def filtered(request):
    # Check if the form has been submitted
    if request.method == 'POST':
        
        # Example input values
        teacher = ''
        batch = ''
        code = ''
        
        # Get the form inputs
        if 'teacher' in request.POST:
            teacher = request.POST['teacher']
        if 'batch' in request.POST:
            batch = request.POST['batch']
        if 'code' in request.POST:
            code = request.POST['code']
        
        # Load the Excel sheet from Google Sheets
        time_table_df = pd.read_excel('D:/Django/webtech/playground/templates/sheet.xlsx')

        time_table_df.iloc[:, 0] = time_table_df.iloc[:, 0].ffill()
        time_table_df.fillna('No Class', inplace=True)
        
        if teacher:
            time_table_df = time_table_df[time_table_df.apply(lambda x: x.astype(str).str.contains(teacher, case=False, regex=False).any(), axis=1)]
            replace_dict = {col: rf'^(?!.*{teacher}).*$' for col in time_table_df.columns[1:]}
            time_table_df.replace(replace_dict, 'No Class', regex=True, inplace=True)           
        if batch:
            time_table_df = time_table_df[time_table_df.apply(lambda x: x.astype(str).str.contains(batch, case=False, regex=False).any(), axis=1)]
            replace_dict = {col: rf'^(?!.*{batch}).*$' for col in time_table_df.columns[1:]}
            time_table_df.replace(replace_dict, 'No Class', regex=True, inplace=True)
        if code:
            time_table_df = time_table_df[time_table_df.apply(lambda x: x.astype(str).str.contains(code, case=False, regex=False).any(), axis=1)]
            replace_dict = {col: rf'^(?!.*{code}).*$' for col in time_table_df.columns[1:]}
            time_table_df.replace(replace_dict, 'No Class', regex=True, inplace=True)
        
        # for col in time_table_df:
        #     df = time_table_df
        #     # time_list = time_table_df.iloc[0].tolist()
        #     time_list = ['D/T','09:00 AM - 09:55 AM','10:00 AM - 10:55 AM','11:00 AM - 11:55 AM','12:00 PM - 12:55PM','01:00 PM - 01:55 PM','02:00 PM - 02:55 PM','03:00 PM - 03:55 PM','04:00PM - 04:55 PM']
        #     # t = (time_table_df == time_list)
        #     zeroes = df.astype(str) == time_list
        #     # re = t[t].index.to_list()
        #     nans = (df.isna()) & (df.applymap(type) != type(None))
        #     last  = nans|zeroes
        #     cols = last.all()[last.all()].index.to_list()
        #     # if time_table_df[col].isnull() and time_table_df[col] in time_list.all():
        #     time_table_df.drop(cols, axis=1)

        # Convert the filtered data to HTML table
        fil_html = time_table_df.to_html(index=False)

        # Render the filtered time table HTML template
        return render(request, 'filtered.html', {'fil_html': fil_html})

    # If the form hasn't been submitted, redirect to the full time table page
    else:
        return redirect('timetable')   