const container = document.querySelector('.container');
let array = [];
let barAmount = 40;

function generateArray(){
    container.innerHTML = ``;
    array = [];
    for (let i = 0; i < barAmount; i++){
        const val = Math.floor(Math.random() * 250) + 10;
        array.push(val);
        const bar = document.createElement('div');
        bar.classList.add('bar');
        bar.style.height = `${val}px`;
        container.appendChild(bar);
    };
};

function sleep(ms){
    return new Promise(resolve => setTimeout(resolve, ms));
};

async function sort() {
    const bars = document.querySelectorAll('.bar');
    const sortBtn = document.querySelector('.sortBtn');
    const newArray = document.querySelector('.newArray');

    sortBtn.disabled = true;
    newArray.disabled = true;
    sortBtn.style.opacity = '0.5';
    newArray.style.opacity = '0.5';

    for (let i = 0; i < array.length; i++){
        for (let j = 0; j < array.length - i - 1; j++){
            bars[j].style.backgroundColor = "#e74c3c";
            bars[j + 1].style.backgroundColor = "#e74c3c";

            if (array[j] > array[j + 1]){
                let temp = array[j];
                array[j] = array[j + 1];
                array[j + 1] = temp;
                bars[j].style.height = `${array[j]}px`;
                bars[j + 1].style.height = `${array[j + 1]}px`;
            };

            await sleep(40);

            bars[j].style.backgroundColor = "#3498db";
            bars[j + 1].style.backgroundColor = "#3498db";
        };
        bars[array.length - i - 1].style.backgroundColor = "#27ae60";
    };
    sortBtn.disabled = false;
    newArray.disabled = false;
    sortBtn.style.opacity = "1";
    newArray.style.opacity = "1";
};

generateArray();