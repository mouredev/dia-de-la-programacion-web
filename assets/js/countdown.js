var countDownDate = new Date("September 12, 2024 14:00:00 UTC").getTime();

var x = setInterval(function () {

    var now = new Date().getTime();
    var distance = countDownDate - now;

    var days = Math.floor(distance / (1000 * 60 * 60 * 24));
    var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((distance % (1000 * 60)) / 1000);

    document.getElementById("countdown_days").innerHTML = days.toString().padStart(2, '0')
    document.getElementById("countdown_hours").innerHTML = hours.toString().padStart(2, '0')
    document.getElementById("countdown_minutes").innerHTML = minutes.toString().padStart(2, '0')
    document.getElementById("countdown_seconds").innerHTML = seconds.toString().padStart(2, '0')

    if (distance < 0) {
        clearInterval(x);
        document.getElementById("countdown").style.display = "none";
    }
}, 1000);