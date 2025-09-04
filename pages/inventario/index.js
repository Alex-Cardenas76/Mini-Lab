import React, { useState, useEffect } from 'react';
import {
    Box,
    Grid,
    Card,
    CardContent,
    Typography,
    Button,
    Table,
    TableBody,
    TableCell,
    TableContainer,
    TableHead,
    TableRow,
    Paper,
    Alert,
    IconButton,
    Dialog,
    DialogTitle,
    DialogContent,
    DialogActions,
    TextField,
    Select,
    MenuItem,
    FormControl,
    InputLabel,
    Tabs,
    Tab,
    Chip
} from '@mui/material';
import AddIcon from '@mui/icons-material/Add';
import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';
import VisibilityIcon from '@mui/icons-material/Visibility';
import WarningIcon from '@mui/icons-material/Warning';

const DashboardInventario = () => {
    const [activeTab, setActiveTab] = useState(0);
    const [alertas, setAlertas] = useState([]);
    const [resumen, setResumen] = useState({});
    const [openDialog, setOpenDialog] = useState(false);
    const [selectedItem, setSelectedItem] = useState(null);
    const [formData, setFormData] = useState({});
    const [currentSection, setCurrentSection] = useState('');

    // Estados para cada sección
    const [varillas, setVarillas] = useState([]);
    const [pinturas, setPinturas] = useState([]);
    const [materialesImpresion, setMaterialesImpresion] = useState([]);
    const [materialesRecordatorio, setMaterialesRecordatorio] = useState([]);
    const [software, setSoftware] = useState([]);
    const [materialesPintura, setMaterialesPintura] = useState([]);
    const [materialesDiseno, setMaterialesDiseno] = useState([]);
    const [productosTerminados, setProductosTerminados] = useState([]);

    // Cargar datos iniciales
    useEffect(() => {
        cargarDatos();
    }, []);

    const cargarDatos = async () => {
        try {
            const [alertasData, resumenData] = await Promise.all([
                fetch('/api/inventario/alertas').then(res => res.json()),
                fetch('/api/inventario/resumen').then(res => res.json())
            ]);
            setAlertas(alertasData);
            setResumen(resumenData);
        } catch (error) {
            console.error('Error al cargar datos:', error);
        }
    };

    const handleTabChange = (event, newValue) => {
        setActiveTab(newValue);
        cargarSeccion(newValue);
    };

    const cargarSeccion = async (tabIndex) => {
        try {
            let endpoint = '';
            switch (tabIndex) {
                case 0: // Varillas
                    endpoint = '/api/inventario/varillas';
                    break;
                case 1: // Pinturas
                    endpoint = '/api/inventario/pinturas';
                    break;
                case 2: // Materiales Impresión
                    endpoint = '/api/inventario/materiales-impresion';
                    break;
                case 3: // Materiales Recordatorio
                    endpoint = '/api/inventario/materiales-recordatorio';
                    break;
                case 4: // Software
                    endpoint = '/api/inventario/software';
                    break;
                case 5: // Materiales Pintura
                    endpoint = '/api/inventario/materiales-pintura';
                    break;
                case 6: // Materiales Diseño
                    endpoint = '/api/inventario/materiales-diseno';
                    break;
                case 7: // Productos Terminados
                    endpoint = '/api/inventario/productos-terminados';
                    break;
                default:
                    return;
            }
            const data = await fetch(endpoint).then(res => res.json());
            actualizarEstadoSeccion(tabIndex, data);
        } catch (error) {
            console.error('Error al cargar sección:', error);
        }
    };

    const actualizarEstadoSeccion = (tabIndex, data) => {
        switch (tabIndex) {
            case 0:
                setVarillas(data);
                break;
            case 1:
                setPinturas(data);
                break;
            case 2:
                setMaterialesImpresion(data);
                break;
            case 3:
                setMaterialesRecordatorio(data);
                break;
            case 4:
                setSoftware(data);
                break;
            case 5:
                setMaterialesPintura(data);
                break;
            case 6:
                setMaterialesDiseno(data);
                break;
            case 7:
                setProductosTerminados(data);
                break;
        }
    };

    const handleCrear = (seccion) => {
        setCurrentSection(seccion);
        setSelectedItem(null);
        setFormData({});
        setOpenDialog(true);
    };

    const handleEditar = (item, seccion) => {
        setCurrentSection(seccion);
        setSelectedItem(item);
        setFormData(item);
        setOpenDialog(true);
    };

    const handleEliminar = async (id, seccion) => {
        if (window.confirm('¿Estás seguro de que quieres eliminar este elemento?')) {
            try {
                const endpoint = `/api/inventario/${seccion}/${id}`;
                await fetch(endpoint, { method: 'DELETE' });
                cargarSeccion(activeTab);
                cargarDatos();
            } catch (error) {
                console.error('Error al eliminar:', error);
            }
        }
    };

    const handleSubmit = async () => {
        try {
            const method = selectedItem ? 'PUT' : 'POST';
            const endpoint = selectedItem 
                ? `/api/inventario/${currentSection}/${selectedItem._id}`
                : `/api/inventario/${currentSection}`;

            const response = await fetch(endpoint, {
                method,
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(formData)
            });

            if (response.ok) {
                setOpenDialog(false);
                cargarSeccion(activeTab);
                cargarDatos();
            }
        } catch (error) {
            console.error('Error al guardar:', error);
        }
    };

    const renderTablaVarillas = () => (
        <TableContainer component={Paper}>
            <Table>
                <TableHead>
                    <TableRow>
                        <TableCell>Nombre de la Moldura</TableCell>
                        <TableCell>Ancho (cm)</TableCell>
                        <TableCell>Alto (cm)</TableCell>
                        <TableCell>Material</TableCell>
                        <TableCell>Estilo</TableCell>
                        <TableCell>Stock Actual</TableCell>
                        <TableCell>Stock Mínimo</TableCell>
                        <TableCell>Acciones</TableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                    {varillas.map((varilla) => (
                        <TableRow key={varilla._id}>
                            <TableCell>{varilla.nombre}</TableCell>
                            <TableCell>{varilla.ancho}</TableCell>
                            <TableCell>{varilla.alto}</TableCell>
                            <TableCell>{varilla.material}</TableCell>
                            <TableCell>{varilla.estilo}</TableCell>
                            <TableCell>
                                <Chip 
                                    label={varilla.stockActual}
                                    color={varilla.stockActual <= varilla.stockMinimo ? 'error' : 'success'}
                                />
                            </TableCell>
                            <TableCell>{varilla.stockMinimo}</TableCell>
                            <TableCell>
                                <IconButton onClick={() => handleEditar(varilla, 'varillas')}>
                                    <EditIcon />
                                </IconButton>
                                <IconButton onClick={() => handleEliminar(varilla._id, 'varillas')}>
                                    <DeleteIcon />
                                </IconButton>
                            </TableCell>
                        </TableRow>
                    ))}
                </TableBody>
            </Table>
        </TableContainer>
    );

    const renderTablaPinturas = () => (
        <TableContainer component={Paper}>
            <Table>
                <TableHead>
                    <TableRow>
                        <TableCell>Producto</TableCell>
                        <TableCell>Tipo</TableCell>
                        <TableCell>Stock Actual</TableCell>
                        <TableCell>Stock Mínimo</TableCell>
                        <TableCell>Unidad</TableCell>
                        <TableCell>Acciones</TableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                    {pinturas.map((pintura) => (
                        <TableRow key={pintura._id}>
                            <TableCell>{pintura.producto}</TableCell>
                            <TableCell>{pintura.tipo}</TableCell>
                            <TableCell>
                                <Chip 
                                    label={`${pintura.stockActual} ${pintura.unidad}`}
                                    color={pintura.stockActual <= pintura.stockMinimo ? 'error' : 'success'}
                                />
                            </TableCell>
                            <TableCell>{pintura.stockMinimo}</TableCell>
                            <TableCell>{pintura.unidad}</TableCell>
                            <TableCell>
                                <IconButton onClick={() => handleEditar(pintura, 'pinturas')}>
                                    <EditIcon />
                                </IconButton>
                                <IconButton onClick={() => handleEliminar(pintura._id, 'pinturas')}>
                                    <DeleteIcon />
                                </IconButton>
                            </TableCell>
                        </TableRow>
                    ))}
                </TableBody>
            </Table>
        </TableContainer>
    );

    const renderTablaGenerica = (data, columnas) => (
        <TableContainer component={Paper}>
            <Table>
                <TableHead>
                    <TableRow>
                        {columnas.map(col => (
                            <TableCell key={col}>{col}</TableCell>
                        ))}
                        <TableCell>Acciones</TableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                    {data.map((item) => (
                        <TableRow key={item._id}>
                            {columnas.map(col => (
                                <TableCell key={col}>
                                    {col === 'Stock Actual' ? (
                                        <Chip 
                                            label={`${item.stockActual} ${item.unidad || ''}`}
                                            color={item.stockActual <= item.stockMinimo ? 'error' : 'success'}
                                        />
                                    ) : (
                                        item[col.toLowerCase().replace(/\s+/g, '')] || item[col]
                                    )}
                                </TableCell>
                            ))}
                            <TableCell>
                                <IconButton onClick={() => handleEditar(item, currentSection)}>
                                    <EditIcon />
                                </IconButton>
                                <IconButton onClick={() => handleEliminar(item._id, currentSection)}>
                                    <DeleteIcon />
                                </IconButton>
                            </TableCell>
                        </TableRow>
                    ))}
                </TableBody>
            </Table>
        </TableContainer>
    );

    const tabs = [
        { label: 'Varillas/Molduras', data: varillas, columnas: ['Producto', 'Unidad', 'Stock Actual', 'Stock Mínimo'] },
        { label: 'Pinturas y Acabados', data: pinturas, columnas: ['Producto', 'Tipo', 'Stock Actual', 'Stock Mínimo', 'Unidad'] },
        { label: 'Materiales Impresión', data: materialesImpresion, columnas: ['Producto', 'Unidad', 'Stock Actual', 'Stock Mínimo'] },
        { label: 'Materiales Recordatorio', data: materialesRecordatorio, columnas: ['Producto', 'Unidad', 'Stock Actual', 'Stock Mínimo'] },
        { label: 'Software y Equipos', data: software, columnas: ['Producto', 'Unidad', 'Stock Actual', 'Stock Mínimo'] },
        { label: 'Materiales Pintura', data: materialesPintura, columnas: ['Producto', 'Unidad', 'Stock Actual', 'Stock Mínimo'] },
        { label: 'Materiales Diseño', data: materialesDiseno, columnas: ['Producto', 'Unidad', 'Stock Actual', 'Stock Mínimo'] },
        { label: 'Productos Terminados', data: productosTerminados, columnas: ['Nombre', 'Tipo', 'Stock Actual', 'Estado', 'Precio'] }
    ];

    return (
        <Box sx={{ p: 3 }}>
            {/* Resumen de Inventario */}
            <Grid container spacing={3} sx={{ mb: 3 }}>
                <Grid item xs={12} md={3}>
                    <Card>
                        <CardContent>
                            <Typography variant="h6">Total Varillas</Typography>
                            <Typography variant="h4">{resumen.totalVarillas || 0}</Typography>
                        </CardContent>
                    </Card>
                </Grid>
                <Grid item xs={12} md={3}>
                    <Card>
                        <CardContent>
                            <Typography variant="h6">Total Pinturas</Typography>
                            <Typography variant="h4">{resumen.totalPinturas || 0}</Typography>
                        </CardContent>
                    </Card>
                </Grid>
                <Grid item xs={12} md={3}>
                    <Card>
                        <CardContent>
                            <Typography variant="h6">Stock Bajo</Typography>
                            <Typography variant="h4" color="error">
                                {alertas.length}
                            </Typography>
                        </CardContent>
                    </Card>
                </Grid>
                <Grid item xs={12} md={3}>
                    <Card>
                        <CardContent>
                            <Typography variant="h6">Productos Terminados</Typography>
                            <Typography variant="h4">{resumen.totalProductosTerminados || 0}</Typography>
                        </CardContent>
                    </Card>
                </Grid>
            </Grid>

            {/* Alertas de Stock Bajo */}
            {alertas.length > 0 && (
                <Box sx={{ mb: 3 }}>
                    <Typography variant="h6" sx={{ mb: 2 }}>
                        Alertas de Stock Bajo
                    </Typography>
                    {alertas.map((alerta, index) => (
                        <Alert 
                            key={index} 
                            severity="warning" 
                            sx={{ mb: 1 }}
                            icon={<WarningIcon />}
                        >
                            {alerta.tipo}: {alerta.producto} - Stock actual {alerta.stockActual} (Mínimo: {alerta.stockMinimo})
                        </Alert>
                    ))}
                </Box>
            )}

            {/* Tabs de Secciones */}
            <Box sx={{ borderBottom: 1, borderColor: 'divider', mb: 2 }}>
                <Tabs value={activeTab} onChange={handleTabChange}>
                    {tabs.map((tab, index) => (
                        <Tab key={index} label={tab.label} />
                    ))}
                </Tabs>
            </Box>

            {/* Botón Agregar */}
            <Box sx={{ mb: 2 }}>
                <Button 
                    variant="contained" 
                    startIcon={<AddIcon />}
                    onClick={() => handleCrear(tabs[activeTab].label.toLowerCase().replace(/\s+/g, '-'))}
                >
                    Agregar {tabs[activeTab].label}
                </Button>
            </Box>

            {/* Contenido de la Tab */}
            <Box>
                {activeTab === 0 && renderTablaVarillas()}
                {activeTab === 1 && renderTablaPinturas()}
                {activeTab > 1 && renderTablaGenerica(tabs[activeTab].data, tabs[activeTab].columnas)}
            </Box>

            {/* Diálogo para Crear/Editar */}
            <Dialog open={openDialog} onClose={() => setOpenDialog(false)} maxWidth="md" fullWidth>
                <DialogTitle>
                    {selectedItem ? 'Editar' : 'Crear'} {tabs[activeTab].label}
                </DialogTitle>
                <DialogContent>
                    <Grid container spacing={2} sx={{ mt: 1 }}>
                        {activeTab === 0 && (
                            <>
                                <Grid item xs={12} md={6}>
                                    <TextField
                                        fullWidth
                                        label="Nombre de la Moldura"
                                        value={formData.nombre || ''}
                                        onChange={(e) => setFormData({...formData, nombre: e.target.value})}
                                    />
                                </Grid>
                                <Grid item xs={12} md={3}>
                                    <TextField
                                        fullWidth
                                        label="Ancho (cm)"
                                        type="number"
                                        value={formData.ancho || ''}
                                        onChange={(e) => setFormData({...formData, ancho: Number(e.target.value)})}
                                    />
                                </Grid>
                                <Grid item xs={12} md={3}>
                                    <TextField
                                        fullWidth
                                        label="Alto (cm)"
                                        type="number"
                                        value={formData.alto || ''}
                                        onChange={(e) => setFormData({...formData, alto: Number(e.target.value)})}
                                    />
                                </Grid>
                                <Grid item xs={12} md={6}>
                                    <TextField
                                        fullWidth
                                        label="Material"
                                        value={formData.material || ''}
                                        onChange={(e) => setFormData({...formData, material: e.target.value})}
                                    />
                                </Grid>
                                <Grid item xs={12} md={6}>
                                    <TextField
                                        fullWidth
                                        label="Estilo"
                                        value={formData.estilo || ''}
                                        onChange={(e) => setFormData({...formData, estilo: e.target.value})}
                                    />
                                </Grid>
                            </>
                        )}
                        <Grid item xs={12} md={6}>
                            <TextField
                                fullWidth
                                label="Stock Actual"
                                type="number"
                                value={formData.stockActual || ''}
                                onChange={(e) => setFormData({...formData, stockActual: Number(e.target.value)})}
                            />
                        </Grid>
                        <Grid item xs={12} md={6}>
                            <TextField
                                fullWidth
                                label="Stock Mínimo"
                                type="number"
                                value={formData.stockMinimo || ''}
                                onChange={(e) => setFormData({...formData, stockMinimo: Number(e.target.value)})}
                            />
                        </Grid>
                    </Grid>
                </DialogContent>
                <DialogActions>
                    <Button onClick={() => setOpenDialog(false)}>Cancelar</Button>
                    <Button onClick={handleSubmit} variant="contained">Guardar</Button>
                </DialogActions>
            </Dialog>
        </Box>
    );
};

export default DashboardInventario; 