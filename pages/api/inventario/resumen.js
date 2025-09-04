import { connectDB } from '../../../lib/db';
import { 
    Varilla, 
    PinturaAcabado, 
    MaterialImpresion, 
    MaterialRecordatorio, 
    SoftwareEquipo, 
    MaterialPintura, 
    MaterialDiseno, 
    ProductoTerminado 
} from '../../../models/Inventory';

export default async function handler(req, res) {
    if (req.method !== 'GET') {
        return res.status(405).json({ error: 'Método no permitido' });
    }

    try {
        await connectDB();

        const [
            totalVarillas,
            totalPinturas,
            totalMaterialesImpresion,
            totalMaterialesRecordatorio,
            totalSoftware,
            totalMaterialesPintura,
            totalMaterialesDiseno,
            totalProductosTerminados
        ] = await Promise.all([
            Varilla.countDocuments(),
            PinturaAcabado.countDocuments(),
            MaterialImpresion.countDocuments(),
            MaterialRecordatorio.countDocuments(),
            SoftwareEquipo.countDocuments(),
            MaterialPintura.countDocuments(),
            MaterialDiseno.countDocuments(),
            ProductoTerminado.countDocuments()
        ]);

        const resumen = {
            totalVarillas,
            totalPinturas,
            totalMaterialesImpresion,
            totalMaterialesRecordatorio,
            totalSoftware,
            totalMaterialesPintura,
            totalMaterialesDiseno,
            totalProductosTerminados
        };

        res.status(200).json(resumen);
    } catch (error) {
        console.error('Error al obtener resumen:', error);
        res.status(500).json({ error: 'Error al obtener resumen del inventario' });
    }
} 