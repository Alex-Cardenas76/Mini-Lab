import { connectDB } from '../../../lib/db';
import { Varilla } from '../../../models/Inventory';

export default async function handler(req, res) {
    await connectDB();

    switch (req.method) {
        case 'GET':
            try {
                const varillas = await Varilla.find().sort({ nombre: 1 });
                res.status(200).json(varillas);
            } catch (error) {
                res.status(500).json({ error: 'Error al obtener varillas' });
            }
            break;

        case 'POST':
            try {
                const varilla = new Varilla(req.body);
                await varilla.save();
                res.status(201).json(varilla);
            } catch (error) {
                res.status(500).json({ error: 'Error al crear varilla' });
            }
            break;

        default:
            res.status(405).json({ error: 'Método no permitido' });
    }
} 