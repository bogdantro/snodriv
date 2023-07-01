function hallOfFame(){
    document.getElementById('hallOfFameChoices').classList.add('active');
}

function hallOfFameClose(){
    document.getElementById('hallOfFameChoices').classList.remove('active');
}


function cat(){
    document.getElementById('catChoices').classList.add('active');
}

function tbbExtra(){
    document.getElementById('tbbExtraSide').classList.add('active');

    document.getElementById('fiberExtraSide').classList.remove('active');
    document.getElementById('densExtraSide').classList.remove('active');
}

function fiberExtra(){
    document.getElementById('fiberExtraSide').classList.add('active');

    document.getElementById('tbbExtraSide').classList.remove('active');
    document.getElementById('densExtraSide').classList.remove('active');
}

function densExtra(){
    document.getElementById('densExtraSide').classList.add('active');

    document.getElementById('fiberExtraSide').classList.remove('active');
    document.getElementById('tbbExtraSide').classList.remove('active');
}

function catClose(){
    document.getElementById('catChoices').classList.remove('active');
    document.getElementById('fiberExtraSide').classList.remove('active');
    document.getElementById('tbbExtraSide').classList.remove('active');
    document.getElementById('densExtraSide').classList.remove('active');
}