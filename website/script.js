// Read the CSV file using the Fetch API
fetch('forecast.csv')
	.then(response => response.text())
	.then(data => {
		// Split the CSV data into lines
		const lines = data.split('\n');
		// Create an array to store the table rows
		const rows = [];
		// Loop through each line
		for (let i = 1; i < lines.length; i++) {
			// Split the line into fields
			const fields = lines[i].split(',');
			// Add a new table row for each line
			const row = document.createElement('tr');
			// Add the date and AQI fields as table cells
			const dateCell = document.createElement('td');
			dateCell.textContent = fields[0];
			row.appendChild(dateCell);
			const aqiCell = document.createElement('td');
			aqiCell.textContent = fields[1];
			row.appendChild(aqiCell);
			// Add the row to the table
			rows.push(row);
		}
		// Get the table body element
		const tableBody = document.getElementById('forecastTable');
		// Add each row to the table body
		for (let i = 0; i < rows.length; i++) {
			tableBody.appendChild(rows[i]);
		}
	});