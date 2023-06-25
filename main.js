const ctxP = document.getElementById("pulseChart").getContext("2d");
const ctxO = document.getElementById("oxygenChart").getContext("2d");

let delayed;

//Gradiant Fill
let gradientPulse = ctxP.createLinearGradient(0, 0, 0, 400);
gradientPulse.addColorStop(0, "#540b36");
gradientPulse.addColorStop(1, "#c31432");

let gradientOxygen = ctxO.createLinearGradient(0, 0, 0, 400);
gradientOxygen.addColorStop(0, "#001D74");
gradientOxygen.addColorStop(1, "#2FB4E0");

const labels = [
    '0',
    '1',
    '2',
    '3',
    '4',
    '5',
];

const pulseData = {
    labels,
    datasets: [
    {
        data: [56, 60, 34, 57, 43, 45],
        label: "Pulse",
        fill: true,
        backgroundColor: gradientPulse,
        borderColor: "#fff",
        pointBackgroundColor: "rgb(189, 195, 199)",
        tension: 0.35,
    },
  ]
};

const pulseConfig = {
    type: 'line',
    data: pulseData,
    options: {
        radius: 5,
        hitRadius: 30,
        hoverRadius: 7,
        responsive: true,
        maintainAspectRatio: false,
        animation: {
            onComplete: () => {
            delayed = true;
        },
        delay: (context) => {
        let delay = 0;
        if (context.type === 'data' && context.mode === 'default' && !delayed) {
          delay = context.dataIndex * 300 + context.datasetIndex * 100;
        }
        return delay;
      },
    },

    scales: {
        y: {
          ticks: {
            callback: function (yValue){
              return yValue + ' bpm';
          }
        }
      },
      x: {
          ticks: {
            callback: function (xValue){
              return xValue + 's';
          }
        }
      }
    },
  },
};

//==============================================================================

const oxygenData = {
    labels,
    datasets: [
    {
        data: [93, 94, 97, 89, 91, 99],
        label: "sO2",
        fill: true,
        backgroundColor: gradientOxygen,
        borderColor: "#fff",
        pointBackgroundColor: "rgb(189, 195, 199)",
        tension: 0.35,
    },
  ]
};

const oxygenConfig = {
    type: 'line',
    data: oxygenData,
    options: {
        radius: 5,
        hitRadius: 30,
        hoverRadius: 7,
        responsive: true,
        maintainAspectRatio: false,
        animation: {
            onComplete: () => {
            delayed = true;
        },
        delay: (context) => {
            let delay = 0;
            if (context.type === 'data' && context.mode === 'default' && !delayed) {
            delay = context.dataIndex * 300 + context.datasetIndex * 100;
        }
        return delay;
      },
    },

    scales: {
        y: {
          ticks: {
            callback: function (yValue){
              return yValue + ' mmHg';
          }
        }
      },
      x: {
          ticks: {
            callback: function (xValue){
              return xValue + 's';
          }
        }
      }
    },
  },
};

const pulseChart = new Chart(ctxP, pulseConfig);
const oxygenChart = new Chart(ctxO, oxygenConfig);