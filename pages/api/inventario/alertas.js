import { connectDB } from '../../../lib/db';
import { Varilla } from '../../../models/Inventory';

export default async function handler(req, res) {
    if (req.method !== 'GET') {
        return res.status(405).json({ error: 'Método no permitido' });
    }

    try {
        await connectDB();

        const varillasStockBajo = await Varilla.find({
            $expr: {
                $lte: ['$stock', '$stockMinimo']
            }
        });

        const alertas = varillasStockBajo.map(varilla => ({
            modelo: varilla.modelo,
            stockActual: varilla.stock,
            stockMinimo: varilla.stockMinimo,
            faltante: varilla.stockMinimo - varilla.stock
        }));

        res.status(200).json(alertas);
    } catch (error) {
        console.error('Error al obtener alertas:', error);
        res.status(500).json({ error: 'Error al obtener alertas de inventario' });
    }
} 