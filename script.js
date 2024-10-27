let events = []; // Carregue os dados do JSON nesta variável

// Função para carregar o arquivo JSON e exibir todos os eventos
fetch('3.Eventos_Organizados.json')
    .then(response => response.json())
    .then(data => {
        events = data;
        displayEvents(events);
    })
    .catch(error => console.error('Erro ao carregar os eventos:', error));

// Função para exibir eventos no container
function displayEvents(eventsToShow) {
    const eventsContainer = document.getElementById('eventsContainer');
    const resultCount = document.getElementById('resultCount');
    eventsContainer.innerHTML = '';

    eventsToShow.forEach(event => {
        const eventCard = document.createElement('div');
        eventCard.className = 'event-card';
        eventCard.innerHTML = `
            <h3>${event.Trilha}</h3>
            <p><strong>Data:</strong> ${event.Data}</p>
            <p><strong>Horário:</strong> ${event.Horário}</p>
            <p><strong>Local:</strong> ${event.Local}</p>
            <p><strong>Palestrantes:</strong> ${event.Título}</p>
            <p><strong>Descrição:</strong> ${event.Descrição}</p>
        `;
        eventsContainer.appendChild(eventCard);
    });

    resultCount.textContent = eventsToShow.length;
}

// Função para filtrar eventos
function filterEvents() {
    const searchInput = document.getElementById('searchInput').value.toLowerCase();
    const dateFilter = document.getElementById('dateFilter').value;
    const auditoriumFilter = document.getElementById('auditoriumFilter').value;
    const speakerFilter = document.getElementById('speakerFilter').value.toLowerCase();
    const trackFilter = document.getElementById('trackFilter').value;
    const sortFilter = document.getElementById('sortFilter').value;

    let filteredEvents = events.filter(event => {
        return (
            (searchInput === '' || event.Título.toLowerCase().includes(searchInput)) &&
            (dateFilter === '' || event.Data === dateFilter) &&
            (auditoriumFilter === '' || event.Local === auditoriumFilter) &&
            (speakerFilter === '' || event.Título.toLowerCase().includes(speakerFilter)) &&
            (trackFilter === '' || event.Trilha === trackFilter)
        );
    });

    // Ordenação dos eventos conforme o filtro selecionado
    if (sortFilter === 'data') {
        filteredEvents.sort((a, b) => new Date(a.Data) - new Date(b.Data));
    } else if (sortFilter === 'auditório') {
        filteredEvents.sort((a, b) => a.Local.localeCompare(b.Local));
    } else if (sortFilter === 'palestraAZ') {
        filteredEvents.sort((a, b) => a.Título.localeCompare(b.Título));
    } else if (sortFilter === 'palestraZA') {
        filteredEvents.sort((a, b) => b.Título.localeCompare(a.Título));
    }

    displayEvents(filteredEvents);
}

// Função para limpar os filtros
function clearFilters() {
    document.getElementById('searchInput').value = '';
    document.getElementById('dateFilter').value = '';
    document.getElementById('auditoriumFilter').value = '';
    document.getElementById('speakerFilter').value = '';
    document.getElementById('trackFilter').value = '';
    document.getElementById('sortFilter').value = 'data';
    displayEvents(events);
}
