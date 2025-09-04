const mongoose = require('mongoose');

const movimientoInventarioSchema = new mongoose.Schema({
    varilla: {
        type: mongoose.Schema.Types.ObjectId,
        ref: 'Varilla',
        required: true
    },
    tipo: {
        type: String,
        enum: ['ENTRADA', 'SALIDA'],
        required: true
    },
    cantidad: {
        type: Number,
        required: true
    },
    motivo: {
        type: String,
        required: true
    },
    ordenProduccion: {
        type: mongoose.Schema.Types.ObjectId,
        ref: 'OrdenProduccion'
    },
    usuario: {
        type: String,
        required: true
    },
    fecha: {
        type: Date,
        default: Date.now
    },
    stockAnterior: Number,
    stockNuevo: Number,
    observaciones: String
});

const MovimientoInventario = mongoose.model('MovimientoInventario', movimientoInventarioSchema);

module.exports = {
    MovimientoInventario
}; 