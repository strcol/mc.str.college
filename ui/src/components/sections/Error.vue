<template>
    <div class="centerize" id="error">
        <i class="las la-exclamation-circle minecraft-red"></i><br><br>
        <h3>Заявка не отправлена</h3>
        Не удалось отправить заявку<br>
        Пожалуйста, попробуй позже
    </div>
</template>

<style>
.centerize {
    margin: 0 auto;
    text-align: center;
}

.la-exclamation-circle {
    font-size: 144px;
}

.minecraft-red {
    color: rgb(170, 0, 0);
}

@media (max-width: 766px) {
    .la-exclamation-circle {
        font-size: 72px;
    }
}
</style>