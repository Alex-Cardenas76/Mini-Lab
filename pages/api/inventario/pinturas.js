import { connectDB } from '../../../lib/db';
import { PinturaAcabado } from '../../../models/Inventory';

export default async function handler(req, res) {
    await connectDB();

    switch (req.method) {
        case 'GET':
            try {
                const pinturas = await PinturaAcabado.find().sort({ producto: 1 });
                res.status(200).json(pinturas);
            } catch (error) {
                res.status(500).json({ error: 'Error al obtener pinturas y acabados' });
            }
            break;

        case 'POST':
            try {
                const pintura = new PinturaAcabado(req.body);
                await pintura.save();
                res.status(201).json(pintura);
            } catch (error) {
                res.status(500).json({ error: 'Error al crear pintura/acabado' });
            }
            break;

        default:
            res.status(405).json({ error: 'Método no permitido' });
    }
} 