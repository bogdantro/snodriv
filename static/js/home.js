function hallOfFame(){
    document.getElementById('hallOfFameBtn').classList.add('active');

    document.getElementById('competitionBtn').classList.remove('active');
    document.getElementById('historyBtn').classList.remove('active');
}

function competition(){
    document.getElementById('competitionBtn').classList.add('active');

    document.getElementById('hallOfFameBtn').classList.remove('active');
    document.getElementById('historyBtn').classList.remove('active');
}

function history(){
    document.getElementById('historyBtn').classList.add('active');

    document.getElementById('hallOfFameBtn').classList.remove('active');
    document.getElementById('competitionBtn').classList.remove('active');
}