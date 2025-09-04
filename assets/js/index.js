document.addEventListener('DOMContentLoaded', function() {
    // Control del nuevo menú móvil de barra superior
    const menuToggle = document.getElementById('pd-menu-toggle');
    const topbarMenu = document.getElementById('pd-topbar-menu');
    const menuClose = document.getElementById('pd-menu-close');

    if (menuToggle && topbarMenu && menuClose) {
        menuToggle.addEventListener('click', function() {
            topbarMenu.classList.add('active');
        });

        menuClose.addEventListener('click', function() {
            topbarMenu.classList.remove('active');
        });
    }

    document.querySelectorAll('.btn-ver').forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            const pedidoId = this.getAttribute('data-id');
            if (pedidoId) {
                window.location.href = `pedidos.html?ver=${pedidoId}`;
            }
        });
    });

    document.querySelectorAll('.btn-editar').forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            const pedidoId = this.getAttribute('data-id');
            if (pedidoId) {
                window.location.href = `pedidos.html?editar=${pedidoId}`;
            }
        });
    });
});

 // Inicialización de gráficos al cargar el documento
 document.addEventListener('DOMContentLoaded', function() {
    initializeCharts();
    
    // Configurar eventos para generación de reportes
    document.getElementById('generate-report').addEventListener('click', generateReport);
    document.getElementById('export-report').addEventListener('click', exportReport);
});

// Función para inicializar todos los gráficos
function initializeCharts() {
    createServicesChart();
    createClientsChart();
    createTopProductsChart();
    createInventoryChart();
    createProfitabilityChart();
    createCostsVsIncomeChart();
}

// Gráfico de ingresos por servicio
function createServicesChart() {
    const ctx = document.getElementById('services-chart').getContext('2d');
    new Chart(ctx, {
        type: 'pie',
        data: {
            labels: ['Impresión Minilab', 'Recordatorios Escolares', 'Enmarcado', 'Retoque Fotográfico'],
            datasets: [{
                data: [2250, 7200, 4500, 1050],
                backgroundColor: [
                    '#4e73df',
                    '#1cc88a',
                    '#36b9cc',
                    '#f6c23e'
                ],
                hoverBackgroundColor: [
                    '#2e59d9',
                    '#17a673',
                    '#2c9faf',
                    '#dda20a'
                ],
                hoverBorderColor: "rgba(234, 236, 244, 1)",
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            tooltips: {
                callbacks: {
                    label: function(tooltipItem, data) {
                        let dataset = data.datasets[tooltipItem.datasetIndex];
                        let total = dataset.data.reduce((previousValue, currentValue) => previousValue + currentValue);
                        let currentValue = dataset.data[tooltipItem.index];
                        let percentage = Math.floor(((currentValue/total) * 100) + 0.5);
                        return `${data.labels[tooltipItem.index]}: $${currentValue.toLocaleString()} (${percentage}%)`;
                    }
                }
            },
            plugins: {
                legend: {
                    position: 'right',
                }
            }
        }
    });
}
