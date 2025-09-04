const mongoose = require('mongoose');

const cuadroSchema = new mongoose.Schema({
    descripcion: {
        type: String,
        required: true
    },
    estado: {
        type: String,
        enum: ['EN_PRODUCCION', 'EN_ALMACEN', 'EN_TIENDA', 'VENDIDO'],
        default: 'EN_PRODUCCION'
    },
    ubicacion: {
        type: String,
        required: true
    },
    ordenProduccion: {
        type: mongoose.Schema.Types.ObjectId,
        ref: 'OrdenProduccion',
        required: true
    },
    fechaCreacion: {
        type: Date,
        default: Date.now
    },
    fechaVenta: Date,
    precio: Number,
    observaciones: String
});

const Cuadro = mongoose.model('Cuadro', cuadroSchema);

module.exports = {
    Cuadro
}; 