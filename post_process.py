def pat_signon_file(output):
    if output['12_Sign']:
        output['12_Sign'] = 'SIGNATURE ON FILE'
    return output
def diag_pointer(output):
    if output['24E_DiagPtr']:
        output['24E_DiagPtr'] = str(output['24E_DiagPtr']).replace(",", "")
    return output 

def convert_date_format(output):
    if output['24A_FromDate']:
        date_str =  str(output['24A_FromDate'])
        if len(date_str) == 6:
            day = date_str[:2]
            month = date_str[2:4]
            year = date_str[4:]
            if year in ['16', '17', '18', '19','20', '21', '22', '23', '24', '25', '26']:
                year = '20' + year
            date_formatted = day + month + year
            date_str = date_formatted
        output['24A_FromDate'] = date_str
    elif output['24A_ToDate']:      
        date_str =  str(output['24A_ToDate'])
        if len(date_str) == 6:
            day = date_str[:2]
            month = date_str[2:4]
            year = date_str[4:]
            if year in ['16', '17', '18', '19','20', '21', '22', '23', '24', '25', '26']:
                year = '20' + year
            date_formatted = day + month + year
            date_str = date_formatted
        output['24A_ToDate'] = date_str
    return output