<template>
    <div id="app">
        <Header/>
        <div class="wrapper">
            <section class="header-background">
                <div class="navbar-place"></div>
                <div class="section-container" id="main-content">
                    <template v-if="$root.status == 0">
                        <div class="row">
                            <div class="col-md-6 centerize">
                                <Description/>
                            </div>
                            <div class="col-md-6 centerize">
                                <Form/>
                            </div>
                        </div>
                    </template>
                    <template v-else-if="$root.status == 1">
                        <Success/>
                    </template>
                    <template v-else-if="$root.status == 2">
                        <Error/>
                    </template>
                </div>
            </section>
            <Footer/>
        </div>
    </div>
</template>

<script>
import Header from '@/components/sections/Header';
import Footer from '@/components/sections/Footer';

import Description from '@/components/sections/Description';
import Form from '@/components/sections/Form';
import Error from '@/components/sections/Error';
import Success from '@/components/sections/Success';

export default {
    components: {
        Header, Footer, Description, Form, Error, Success
    }
}
</script>

<style>
@font-face {
    font-family: 'minecraft';
    src: url('/fonts/minecraft.eot');
    src: url('/fonts/minecraft.woff') format('woff');
    src: url('/fonts/minecraft.ttf') format('truetype');
    font-display: swap;
}

html, body {
    height: 100%;
}

#app {
    height: 100%;
    font-family: 'minecraft';
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.48);
    color: #ffffff;
}

section {
    width: 100%;
}

.wrapper {
    display: flex;
    min-height: 100%;
    height: auto;
}

.centerize {
    margin: 0 auto;
    text-align: center;
}

.no-webp .header-background {
    background-color: #000000;
    background-image: url('/images/png/background.png');
    background-position: center center;
    background-repeat: no-repeat;
    background-size: cover;
    display: flex;
    align-items: center;
}

.webp .header-background {
    background-color: #000000;
    background-image: url('/images/webp/background.webp');
    background-position: center center;
    background-repeat: no-repeat;
    background-size: cover;
    display: flex;
    align-items: center;
}

.section-container {
    width: 90%;
    margin: 0 auto;
}

.navbar-place {
    height: 90px;
}

@media (max-width: 766px) {
    #main-content {
        padding-top: 200px;
    }
}

@media (max-height: 800px) {
    #main-content {
        padding-top: 200px;
    }
}
</style>
