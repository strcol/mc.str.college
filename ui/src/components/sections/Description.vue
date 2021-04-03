<template>
    <div id="description">
        <div class="title">
            Build Battle в Minecraft
        </div><br>
        <div class="description">
            🔥 Костанайский строительный колледж проводит мероприятие "Build Battle в Minecraft".<br>
            К участию приглашаются ученики 8 и 9 классов школ города Костаная и Костанайской области.<br>
            Ты побываешь в цифровой копии колледжа, где для тебя проведут экскурсию и ознакомят со специальностями. В конце мероприятия тебя ждет мини-игра "Build Battle"<br><br>
            🎁 3 победителя мини-игры "Build Battle" получат сладкие подарки<br>
            🕒 Дата и время мероприятия: 08.04.2021 в 15:00<br><br>
            Все подробности в чате Telegram: <a href="https://t.me/mc_ksk">@mc_ksk</a><br><br>
            <div class="timer-title">До конца приема заявок осталось:</div>
            <div class="timer">{{ timer }}</div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            timer: '',
            ended: false
        }
    },
    methods: {
        getCase(days) {
            let day = 'дней';
            switch (days) {
                case 1:
                case 21:
                case 31:
                    day = 'день';
                    break;
                case 2:
                case 3:
                case 4:
                case 22:
                case 23:
                case 24:
                    day = 'дня';
                    break;
            }
            return day;
        },
        updateTimer() {
            const deadline = new Date('Apr 8, 2021 00:00:00').getTime();
            var e = (new Date).getTime(),
                t = deadline - e,
                n = Math.floor(t / 86400000),
                o = Math.floor(t % 86400000 / 3600000),
                a = Math.floor(t % 3600000 / 60000),
                r = Math.floor(t % 60000 / 1000);
            this.timer = (n >= 10 ? n : '0' + n) + ' ' + this.getCase(n) + ' ' + (o >= 10 ? o : '0' + o) + ' : ' + (a >= 10 ? a : '0' + a) + ' : ' + (r >= 10 ? r : '0' + r);
            if (t < 0) {
                this.timer = '0 дней 00 : 00 : 00';
                this.ended = true;
            }
        }
    },
    mounted() {
        const vm = this;
        vm.updateTimer(), setInterval(function() {
            vm.updateTimer()
        }, 1000);
    }
}
</script>

<style>
#description a {
    color: #bbbbbb;
}

#description a:hover {
    color: #dddddd;
    text-decoration: none;
}

.title {
    font-size: 24px;
}

.description {
    text-align: left;
}

.timer {
    font-size: 36px;
    text-align: center;
}

.timer-title {
    text-align: center;
}
</style>