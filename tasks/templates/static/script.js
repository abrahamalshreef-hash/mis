ript src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
    let activeTimers = {};
    function toggleTimer(id) {
        const btn = document.getElementById(`btn-${id}`);
        const icon = document.getElementById(`icon-${id}`);
        const display = document.getElementById(`display-${id}`);
        if (activeTimers[id]) {
            clearInterval(activeTimers[id].interval);
            saveTimeToDB(id, activeTimers[id].totalSeconds);
            delete activeTimers[id];
            icon.className = 'fas fa-play';
            btn.classList.replace('btn-primary', 'btn-light');
        } else {
            let totalSeconds = parseTime(display.innerText);
            icon.className = 'fas fa-pause';
            btn.classList.replace('btn-light', 'btn-primary');
            activeTimers[id] = {
                totalSeconds: totalSeconds,
                interval: setInterval(() => {
                    activeTimers[id].totalSeconds++;
                    display.innerText = formatTime(activeTimers[id].totalSeconds);
                }, 1000)
            };
        }
    }
    function saveTimeToDB(taskId, seconds) {
        const formData = new FormData();
        formData.append('seconds', seconds);
        fetch(`/update-duration/${taskId}/`, { method: 'POST', body: formData, headers: {'X-CSRFToken': '{{ csrf_token }}'} });
    }
    function parseTime(str) { const p = str.split(':'); return (+p[0]) * 3600 + (+p[1]) * 60 + (+p[2]); }
    function formatTime(s) { return new Date(s * 1000).toISOString().substr(11, 8); }

    new Chart(document.getElementById('reportChart').getContext('2d'), {
        type: 'doughnut',
        data: { datasets: [{ data: [{{ completed_count }}, {{ remaining_count }}], backgroundColor: ['#6366f1', '#e2e8f0'], borderWidth: 0, borderRadius: 15 }] },
        options: { cutout: '80%', plugins: { legend: { display: false } } }
    });

    function confirmDelete(url) {
        Swal.fire({ title: 'هل تريد الحذف؟', icon: 'warning', showCancelButton: true, confirmButtonText: 'حذف', cancelButtonText: 'إلغاء' }).then((result) => { if (result.isConfirmed) window.location.href = url; });
    }
