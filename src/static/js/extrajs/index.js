(function( HomePage, $, undefined ) {
	var crear_equipamiento_chart = function () {
		var ctx = document.getElementById("equipamiento_chart");
		$.post($(ctx).data('url'), function (data) {
			var equipamiento_chart = new Chart(ctx, {
				type: 'bar',
				data: {
					labels: ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"],
					datasets: [{
						label: 'Equipamientos',
						data: data,
						backgroundColor: 'rgba(0, 166, 90, 0.8)',
						borderWidth: 1
					}]
				},
				options: {
					scales: {
						yAxes: [{
							ticks: {
								beginAtZero:true
							}
						}]
					}
				}
			});	
		});
	}

	var crear_equipamiento_calendario = function () {
		$('#equipamiento-calendario').fullCalendar({
			header: {
				left: 'prev,next today',
				center: '',
				right: 'title'
			},

			navLinks: true, 
			eventSources: [
			{
				url: $('#equipamiento-calendario').data('url-validacion'),
				type: 'GET',
				color: 'orange',
				cache: true,
			},
			{
				url: $('#equipamiento-calendario').data('url-equipamiento'),
				type: 'GET',
				color: 'green',
				cache: true,
			}
			]
		});
	}

	HomePage.init = function () {
		if ($('#equipamiento_chart').length) {
			crear_equipamiento_chart();
		}
		if ($('#equipamiento-calendario').length) {
			crear_equipamiento_calendario();
		}
	}
}( window.HomePage = window.HomePage || {}, jQuery ));