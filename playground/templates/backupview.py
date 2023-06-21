import pandas as pd
from django.shortcuts import render, redirect

def timetable(request):
    # Load the Excel sheet from Google Sheets
    file_path = pd.read_excel('D:/Django/webtech/playground/templates/sheet.xlsx')

    # Convert the data to HTML table
    df = pd.read_excel(file_path, sheet_name='BTECH 4 SEM')
    table_html = df.to_html(index=False)

    # Render the full time table HTML template
    return render(request, 'timetable.html', {'table_html': table_html})

def filtered(request):
    # Check if the form has been submitted
    if request.method == 'POST':
        teacher = request.POST.get('teacher')
        batch = request.POST.get('batch')
        code = request.POST.get('code')

        # Load the Excel sheet from Google Sheets
        time_table_df = pd.read_excel('D:/Django/webtech/playground/templates/sheet.xlsx')

        # Filter the data based on form inputs
        if teacher:
            time_table_df = time_table_df[time_table_df.apply(lambda row: teacher in row.astype(str).str.cat(sep=' '), axis=1)]
        if batch:
            time_table_df = time_table_df[time_table_df.apply(lambda row: batch in row.astype(str).str.cat(sep=' '), axis=1)]
        if code:
            time_table_df = time_table_df[time_table_df.apply(lambda row: code in row.astype(str).str.cat(sep=' '), axis=1)]
        
        # Convert the filtered data to HTML table
        fil_html = time_table_df.to_html(index=False)

        # Render the filtered time table HTML template
        return render(request, 'filtered.html', {'fil_html': fil_html})

    # If the form hasn't been submitted, redirect to the full time table page
    else:
        return redirect('time_table')
    

#     from django.shortcuts import redirect, render
# from django.http import HttpResponse
# import pandas as pd

def timetable(request):

            # Get the file path of the Excel sheet
            file_path = 'D:/Django/webtech/playground/templates/sheet.xlsx'
            # Read the Excel sheet C:\Users\91821\Desktop\Py playground\sheet.xlsxeet using pandas
            df = pd.read_excel(file_path, sheet_name='BTECH 4 SEM')
            table_html = df.to_html(index=False)
            return render(request, 'timetable.html', {'table_html': table_html})

def filtered(request):
    # Check if the form has been submitted
    if request.method == 'POST':
        teacher = 'AMN'  # Example input value
        batch = 'CS410'  # Example input value
        code = 'L-18B11CI412'  # Example input value        
        batch = request.POST.get('batch')
        teacher = request.POST.get('teacher')            
        code = request.POST.get('code')

        # Load the Excel sheet from local storage
        time_table_df = pd.read_excel('D:/Django/webtech/playground/templates/sheet.xlsx')

        # Filter the data based on form inputs
        if teacher:
            time_table_df = time_table_df[time_table_df['Teacher'] == teacher]
        if batch:
            time_table_df = time_table_df[time_table_df['Batch'] == batch]
        if code:
            time_table_df = time_table_df[time_table_df['Code'] == code]
        
        # Convert the filtered data to HTML table
        fil_html = time_table_df.to_html(index=False)

        # Render the filtered time table HTML template
        return render(request, 'filtered.html', {'fil_html': fil_html})

    # If the form hasn't been submitted, redirect to the full time table page
    else:
        return redirect('time_table')    
