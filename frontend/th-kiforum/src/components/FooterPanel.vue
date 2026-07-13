<template>
    <v-footer name="footer" class="d-flex align-center justify-center ga-2 flex-wrap flex-grow-1 py-3" color="surface-light" app>
        <v-btn variant="plain"> Here </v-btn>

        <div class="flex-1-0-100 text-center mt-2">
            {{ new Date().getFullYear() }} —
            <strong>
                <a href="https://tzlr.de" target="_blank" rel="noopener noreferrer" variant="text" style="text-decoration: none;">TZLR</a>
            </strong>
        </div>
    </v-footer>
</template>
