function hallOfFame(){
    document.getElementById('hallOfFameChoices').classList.add('active');
}

function hallOfFameDay(){
    document.getElementById('hallOfFameDaySec').classList.add('active');
    
    document.getElementById('hallOfFameChoices').classList.remove('active');

    document.getElementById('hallOfFameWeekSec').classList.remove('active');
    document.getElementById('hallOfFameMonthSec').classList.remove('active');
    document.getElementById('hallOfFameYearSec').classList.remove('active');
    document.getElementById('hallOfFameAllTimeSec').classList.remove('active');
}

function hallOfFameWeek(){
    document.getElementById('hallOfFameWeekSec').classList.add('active');

    document.getElementById('hallOfFameChoices').classList.remove('active');

    document.getElementById('hallOfFameDaySec').classList.remove('active');
    document.getElementById('hallOfFameMonthSec').classList.remove('active');
    document.getElementById('hallOfFameYearSec').classList.remove('active');
    document.getElementById('hallOfFameAllTimeSec').classList.remove('active');
}

function hallOfFameMonth(){
    document.getElementById('hallOfFameMonthSec').classList.add('active');

    document.getElementById('hallOfFameChoices').classList.remove('active');

    document.getElementById('hallOfFameWeekSec').classList.remove('active');
    document.getElementById('hallOfFameDaySec').classList.remove('active');
    document.getElementById('hallOfFameYearSec').classList.remove('active');
    document.getElementById('hallOfFameAllTimeSec').classList.remove('active');
}

function hallOfFameYear(){
    document.getElementById('hallOfFameYearSec').classList.add('active');

    document.getElementById('hallOfFameChoices').classList.remove('active');

    document.getElementById('hallOfFameWeekSec').classList.remove('active');
    document.getElementById('hallOfFameMonthSec').classList.remove('active');
    document.getElementById('hallOfFameDaySec').classList.remove('active');
    document.getElementById('hallOfFameAllTimeSec').classList.remove('active');
}

function hallOfFameAllTime(){
    document.getElementById('hallOfFameAllTimeSec').classList.add('active');

    document.getElementById('hallOfFameChoices').classList.remove('active');

    document.getElementById('hallOfFameWeekSec').classList.remove('active');
    document.getElementById('hallOfFameMonthSec').classList.remove('active');
    document.getElementById('hallOfFameYearSec').classList.remove('active');
    document.getElementById('hallOfFameDaySec').classList.remove('active');
}

function hallOfFameClose(){
    document.getElementById('hallOfFameChoices').classList.remove('active');
}

//

function competition(){
    document.getElementById('competitionBtn').classList.add('active');
}



// 

function history(){
    document.getElementById('historyBtn').classList.add('active');
}