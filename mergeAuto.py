
from pdfrw import PdfReader, PdfWriter, PdfName
import os
from datetime import datetime as dtime
from datetime import timedelta
import os
import schedule
import time
import platform
import shutil
from datetime import date as dt
def merge_pdf_files_pdfrw(pdf_files, output_filename, folderPdfName):
    output = PdfWriter()
    num = 0
    output_acroform = None
    for f in pdf_files:
        input = PdfReader(folderPdfName + '/' + f, verbose=False)
        output.addpages(input.pages)
        # Not all PDFs have an AcroForm node
        if PdfName('AcroForm') in input[PdfName('Root')].keys():
            source_acroform = input[PdfName('Root')][PdfName('AcroForm')]
            if PdfName('Fields') in source_acroform:
                output_formfields = source_acroform[PdfName('Fields')]
            else:
                output_formfields = []
            num2 = 0
            for form_field in output_formfields:
                key = PdfName('T')
                # Field names are in the "(name)" format
                old_name = form_field[key].replace('(', '').replace(')', '')
                form_field[key] = 'FILE_{n}_FIELD_{m}_{on}'.format(
                    n=num, m=num2, on=old_name)
                num2 += 1
            if output_acroform == None:
                # copy the first AcroForm node
                output_acroform = source_acroform
            else:
                for key in source_acroform.keys():
                    # Add new AcroForms keys if output_acroform already existing
                    if key not in output_acroform:
                        output_acroform[key] = source_acroform[key]
                # Add missing font entries in /DR node of source file
                if (PdfName('DR') in source_acroform.keys()) and (PdfName('Font') in source_acroform[PdfName('DR')].keys()):
                    if PdfName('Font') not in output_acroform[PdfName('DR')].keys():
                        # if output_acroform is missing entirely the /Font node under an existing /DR, simply add it
                        output_acroform[PdfName('DR')][PdfName(
                            'Font')] = source_acroform[PdfName('DR')][PdfName('Font')]
                    else:
                        # else add new fonts only
                        for font_key in source_acroform[PdfName('DR')][PdfName('Font')].keys():
                            if font_key not in output_acroform[PdfName('DR')][PdfName('Font')]:
                                output_acroform[PdfName('DR')][PdfName(
                                    'Font')][font_key] = source_acroform[PdfName('DR')][PdfName('Font')][font_key]
            if PdfName('Fields') not in output_acroform:
                output_acroform[PdfName('Fields')] = output_formfields
            else:
                # Add new fields
                output_acroform[PdfName('Fields')] += output_formfields
        num += 1
    output.trailer[PdfName('Root')][PdfName('AcroForm')] = output_acroform
    output.write(folderPdfName.split('/')[0] + '/' + output_filename)
    if platform.system() == 'Windows':
        os.system('wsl rm -fr ' + folderPdfName)
    else:
        os.system('rm -fr ' + folderPdfName)
    print('Done')
    
def job():
    print('Starting merge...')
    dta = dt.today()
    dta =  dta - timedelta(days=1)
    # time.sleep(10)
    eventsName = os.listdir(f'pdf_mega/Sauvegarde/{str(dta)}')
    folderPdfName = 'pdf_temp/pdf/'
    for f in eventsName:
        print('Merge: ' + f)
        try:
            os.makedirs(folderPdfName.split('/')[0])
        except Exception:
            pass
        try:
            os.makedirs(folderPdfName)
        except Exception:
            pass
        
        os.system('cp pdf_mega/Sauvegarde/' + str(dta) + '/' + f + '/*.pdf ' + folderPdfName)
        os.system('cp pdf_mega/Sauvegarde/' + str(dta) + '/' + f + '/Pas_de_carte_vitale/*.pdf ' + folderPdfName)
        # os.system('cp pdf_mega/Sauvegarde_montreuil/' + str(dta) + '/Pharmacie-montreuil-24-24/Positif/*.pdf pdf_mega/pdf_merge_montreuil/pdf/')
        time.sleep(10)
        pdfM = os.listdir(folderPdfName)
        if len(pdfM) == 0:
            pass
        else:
            while True:
                s = len(os.listdir(folderPdfName))
                time.sleep(10)
                if s == len(os.listdir(folderPdfName)):
                    break
                else:
                    pass
            time.sleep(5)
            now = dtime.now()
            dt_string = now.strftime("%d")
            print('Merging...' + dt_string)
            files = os.listdir(folderPdfName)
            merge_pdf_files_pdfrw(files, 'pdf_merge_' + str(f) + '-' + str(int(dt_string) - 1) + '.pdf', folderPdfName)


schedule.every().day.at('00:01').do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
