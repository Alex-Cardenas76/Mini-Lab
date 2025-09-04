const mongoose = require('mongoose');

const detalleOrdenSchema = new mongoose.Schema({
    varilla: {
        type: mongoose.Schema.Types.ObjectId,
        ref: 'Varilla',
        required: true
    },
    cantidadVarillaPlaneada: {
        type: Number,
        required: true,
        min: 1
    },
    cantidadCuadrosPlaneada: {
        type: Number,
        required: true,
        min: 1
    },
    cantidadVarillaUsada: {
        type: Number,
        default: 0
    },
    cantidadCuadrosProducidos: {
        type: Number,
        default: 0
    },
    merma: {
        type: Number,
        default: 0
    }
});

const ordenProduccionSchema = new mongoose.Schema({
    fechaCreacion: {
        type: Date,
        default: Date.now
    },
    solicitadoPor: {
        type: String,
        required: true
    },
    responsableProduccion: {
        type: String,
        required: true
    },
    estado: {
        type: String,
        enum: ['ABIERTA', 'EN_PROCESO', 'CERRADA', 'CANCELADA'],
        default: 'ABIERTA'
    },
    detalles: [detalleOrdenSchema],
    observaciones: String
});

const OrdenProduccion = mongoose.model('OrdenProduccion', ordenProduccionSchema);

module.exports = {
    OrdenProduccion
}; 