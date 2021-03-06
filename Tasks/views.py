from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.utils.datastructures import MultiValueDictKeyError
import pyautogui
import sys

from Tasks.models import PrimaryTasks, UpdatingCompanyDataStepOne, UpdatingCompanyDataStepTwo, CreateNewDataPullFile, MergeNewCompanyData, PeerAndHistoricalChartsSector, LendingClub_Initial_New_Origination_Data_Cleaning
from Tasks.forms import PrimaryTasksForm, UpdatingCompanyDataStepOneForm, UpdatingCompanyDataStepTwoForm, CreateNewDataPullFileForm, MergeNewCompanyDataForm, PeerAndHistoricalChartsSectorForm, LendingClub_Initial_New_Origination_Data_CleaningForm
from .PullBBGFields_New import Update_Step1, Update_Step2, CreateBBGPullFile, MergeNewCompanies
from .HistoricalCharts_New import RunPeerGroupsAndHistoricalChartsSector, LoadFiles
from .InitialCleanFileFromLCWebsite import LCCleanFile

# Create your views here.
def home_page(request):
    avail_tasks = PrimaryTasks.objects.get(id=1)
    #pyautogui.click(28,1053)
    return render(request, 'home.html', {'list': avail_tasks})

def find_updates_annual(request):
    Update_Step1(QuarterOrAnnual = 'Annual')
    return render(request, 'new_task.html')

def find_updates_quarter(request):
    Update_Step1(QuarterOrAnnual = 'Quarter')
    return render(request, 'new_task.html')

def update_annual(request):
    Update_Step2(QuarterOrAnnual = 'Annual')
    return render(request, 'new_task.html')

def update_quarter(request):
    Update_Step2(QuarterOrAnnual = 'Quarter')
    return render(request, 'new_task.html')

def findata_home(request):
    return render(request, 'FinData.html',)




def fin_data_step_two_home(request):
    return render(request, 'fin_data_step_two.html', {'form': UpdatingCompanyDataStepTwoForm()})


def fin_data_update_step_one(request):
    if request.method == 'POST':
        form = UpdatingCompanyDataStepOneForm(data=request.POST)
        if form.is_valid():
            form.save()
            task = UpdatingCompanyDataStepOne.objects.last()
            lenUpdateAnnual = Update_Step1(QuarterOrAnnual = 'Annual',
                     AnnualFile = task.AnnualFile, QuarterFile = task.QuarterFile,
                     AnnualColumns = task.AnnualColumns, QuarterColumns = task.QuarterColumns,
                     FileForTickers = task.FileForTickers, filepathfor_Excel = task.filepathfor_Excel)
            lenUpdateQuarterly = Update_Step1(QuarterOrAnnual = 'Quarterly',
                     AnnualFile = task.AnnualFile, QuarterFile = task.QuarterFile,
                     AnnualColumns = task.AnnualColumns, QuarterColumns = task.QuarterColumns,
                     FileForTickers = task.FileForTickers, filepathfor_Excel = task.filepathfor_Excel)
            print(lenUpdateAnnual)
            print(lenUpdateQuarterly)
            return redirect('/FinData/UpdateStepOne/completed/')
        else:
            return render(request, 'fin_data_step_one.html', {'form': form})
    else:
        return render(request, 'fin_data_step_one.html', {'form': UpdatingCompanyDataStepOneForm()})

def findata_newcompany(request):
    if request.method == 'POST':
        form = CreateNewDataPullFileForm(data=request.POST)
        if form.is_valid():
            form.save()
            task = CreateNewDataPullFile.objects.last()
            tickers = [s.replace("'", "") for s in task.TickersList.split(',')]
            tickers = [s.lstrip() for s in tickers]
            tickers = [s.rstrip() for s in tickers]
            #Annual
            CreateBBGPullFile(tickers, task.filepathfor_Excel, task.sector, task.numperiodsAnnual, task.FileForColumnsAnnual,'Annual')
            #Quarterly
            CreateBBGPullFile(tickers, task.filepathfor_Excel, task.sector, task.numperiodsQuarter, task.FileForColumnsQuarter,'Quarterly')
            return redirect('/FinData/NewCompany/completed/')
        else:
            return render(request, 'FinDataNewCompany.html', {'form': form})
    else:
        return render(request, 'FinDataNewCompany.html', {'form': CreateNewDataPullFileForm()})

def findatamerge_newcompany(request):
    if request.method == 'POST':
        form = MergeNewCompanyDataForm(data=request.POST)
        if form.is_valid():
            form.save()
            task = MergeNewCompanyData.objects.last()
            MergeNewCompanies(task.AnnualFile, task.NewAnnualFile, task.QuarterFile, task.NewQuarterFile)
            return redirect('/FinData/NewCompanyMerge/completed/')
        else:
            return render(request, 'FinDataNewCompanyMerge.html', {'form': form})
    else:
        return render(request, 'FinDataNewCompanyMerge.html', {'form': MergeNewCompanyDataForm()})
        
    
def findata_runcharts(request):
    
    def prep_charts(item):
        item = [s.replace("'", "") for s in item.split(',')]
        item = [s.replace("[", "") for s in item]
        item = [s.replace("]", "") for s in item]
        item = [s.lstrip() for s in item]
        item = [s.rstrip() for s in item]
        return item
    
    
    if request.method == 'POST':
        form = PeerAndHistoricalChartsSectorForm(data=request.POST)
        if form.is_valid():
            form.save()
            task = PeerAndHistoricalChartsSector.objects.last()
            print(task.AnnualFileLoc)
            print(task.QuarterFileLoc)
            print(task.TickersFileLoc)
            (df_all, df_allq, df_allLTM, TickersList) = LoadFiles(AnnualDataFile =  task.AnnualFileLoc, QuarterDataFile = task.QuarterFileLoc, TickerFile = task.TickersFileLoc)

            RunPeerGroupsAndHistoricalChartsSector(AnnualDF = df_all, 
                                                   QuarterDF = df_allq, 
                                                   LTMDF = df_allLTM, 
                                                   MarketData = TickersList,
                                                   BaseSaveLocation = task.BaseSaveLoc,
                                                   HistoricalChartBaseSaveLocation = task.HistoricalChartBaseSaveLoc,
                                                   SavePDFs = True, ShowPDF = False, 
                                                   Sector = task.SectorOrIndustry, 
                                                   DontWork = prep_charts(task.TickerExclusions), 
                                                   OutputToExcel = False, 
                                                   IncludeLTM = task.IncludeLTMData,
                                                   ChartColumns = prep_charts(task.ChartColumns),
                                                   HistoricalChartColumns = prep_charts(task.HistoricalChartColumns),
                                                   BaseSpreadSheetColumns = prep_charts(task.BaseSpreadSheetColumns),
                                                   SectorsToPrint = prep_charts(task.IndustryOptions),
                                                                             )
            return redirect('/FinData/Charts/completed/')
        else:
            return render(request, 'FinDataCharts.html', {'form': form})
    else:
        return render(request, 'FinDataCharts.html', {'form': PeerAndHistoricalChartsSectorForm()})

        
def fin_data_update_step_two(request):
    if request.method == 'POST':
        form = UpdatingCompanyDataStepTwoForm(data=request.POST)
        if form.is_valid():
            form.save()
            task = UpdatingCompanyDataStepTwo.objects.last()
            Update_Step2(QuarterOrAnnual = 'Annual',
                     AnnualFile = task.ExistingAnnualFile, 
                     QuarterFile = task.ExistingQuarterFile,
                     AnnualUpdateFile = task.NewAnnualFile, 
                     QuarterUpdateFile = task.NewQuarterFile)
            Update_Step2(QuarterOrAnnual = 'Quarterly',
                     AnnualFile = task.ExistingAnnualFile, 
                     QuarterFile = task.ExistingQuarterFile,
                     AnnualUpdateFile = task.NewAnnualFile, 
                     QuarterUpdateFile = task.NewQuarterFile)
            return redirect('/FinData/UpdateStepTwo/completed/')
        else:
            return render(request, 'fin_data_step_two.html', {'form': form})
    else:
        return render(request, 'fin_data_step_two.html', {'form': UpdatingCompanyDataStepTwoForm()})
    
def update_step_one(request):
    form = UpdatingCompanyDataStepOneForm(data = request.POST)
    if form.is_valid():
        UpdatingCompanyDataStepOne.objects.create(QuarterOrAnnual=QorA, filepathfor_Excel=Excel_file_path)
        return redirect('FinData/UpdateStepOne/completed')
    else:
        return render(request, 'fin_data_step_one.html', {"form": form})
    
def completed(request):
    return render(request, 'new_task.html')




def LC_new_orig_data_home(request):
    return render(request, 'LC_NewOrigData.html',)


def LC_new_orig_data_clean(request):
    if request.method == 'POST':
        form = LendingClub_Initial_New_Origination_Data_CleaningForm(data=request.POST)
        if form.is_valid():
            form.save()
            task = LendingClub_Initial_New_Origination_Data_Cleaning.objects.last()
            LCCleanFile(task.FileLocation)
            return redirect('/LendingClub/NewOriginationData/InitialClean/completed/')
        else:
            return render(request, 'LC_NewOrigData_Clean.html', {'form': form})
    else:
        return render(request, 'LC_NewOrigData_Clean.html', {'form': LendingClub_Initial_New_Origination_Data_CleaningForm()})