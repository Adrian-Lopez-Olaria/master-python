# 21 Tkinter 🪟

En esta carpeta se trabaja la creación de interfaces gráficas con **Tkinter**, el toolkit estándar de Python para GUIs. Encontrarás ejemplos progresivos: desde abrir una ventana, colocar textos e imágenes, gestionar formularios y datos, hasta construir menús y mostrar alertas.

## 📘 Explicación

### 1. Ventana (01-ventana.py) 🪟

* Creación de la ventana principal de la aplicación.
* Configuración del título, tamaño inicial y posibilidad de redimensionar.
* Asignación del icono de la aplicación (si el sistema lo permite).

### 2. Textos (02-textos.py) 📝

* Uso de `Label` para mostrar textos.
* Personalización de fuentes (tipo, tamaño, estilo), colores y alineación.
* Colocación básica de etiquetas en la ventana.

### 3. Imágenes (03-imagenes.py) 🖼️

* Carga y visualización de imágenes en la interfaz.
* Integración con `PhotoImage` o PIL (si procede) para formatos comunes.
* Uso de los recursos en `imagenes/` (`galaxia.jpg`, `logo-python.ico`, `orientación.png`).

### 4. Posiciones (04-posiciones.py) 📐

* Introducción a los gestores de geometría: `pack`, `grid` y `place`.
* Ejemplos prácticos de cómo distribuir widgets en filas, columnas y posiciones absolutas.

### 5. Marcos (05-marcos.py) 🧱

* Organización de la interfaz con `Frame` para agrupar widgets.
* Anidación de marcos para layouts más complejos y ordenados.

### 6. Formularios (06-formularios.py) 🧾

* Creación de campos de entrada con `Entry` y etiquetas asociadas.
* Botones de acción para enviar o limpiar datos.

### 7. Recoger datos (07-recoger-datos.py) 📥

* Lectura de valores introducidos por el usuario en los campos del formulario.
* Presentación de los datos en pantalla o procesamiento básico.

### 8. Alertas (08-alertas.py) 🔔

* Uso de `messagebox` para mostrar mensajes informativos, de advertencia, error y confirmación.
* Ejemplos de flujos que reaccionan a la respuesta del usuario.

### 9. Ejercicio (09-ejercicio.py) 🧪

* Mini proyecto integrando textos, entradas y botones.
* Práctica guiada para reforzar eventos y layouts.

### 10. Ejercicio Plus (10-ejercicio-plus.py) 🚀

* Versión ampliada del ejercicio anterior con más validaciones o funcionalidades.
* Mejora de la experiencia de usuario y estructura del código.

### 11. Formularios avanzados (11-formularios2.py) 🧠

* Uso de variables de control (`StringVar`, `IntVar`, etc.).
* Validación sencilla y actualización reactiva de la interfaz.

### 12. Menús (12-menus.py) 📜

* Creación de menús de aplicación con `Menu` y submenús.
* Asociación de comandos a opciones de menú y atajos si aplica.

### 13. Proyecto (13-proyecto.py) 🧩

* Mini proyecto integral con ventana fija (no redimensionable) y tamaño mínimo.
* Menú superior con navegación entre pantallas: Inicio, Añadir, Información y Salir.
* Pantalla Inicio: listado de productos usando `ttk.Treeview` (producto y precio).
* Pantalla Añadir: formulario con campos de nombre, precio y descripción; guarda datos en memoria.
* Pantalla Información: datos de autoría y ejemplo de cambio de vista.
* Gestión básica de estado en memoria y refresco del listado al crear un producto.

## 💡 Consejos y tips

- **Mantén referencias de imágenes** 🖼️: guarda el objeto `PhotoImage` en una variable de instancia (o global) para evitar que el recolector de basura lo elimine y la imagen desaparezca.
- **Elige un solo gestor de geometría por contenedor** 📐: no mezcles `pack` y `grid` en el mismo `Frame` para evitar comportamientos inesperados.
- **Variables de control** 🔄: usa `StringVar`, `IntVar`, etc., para enlazar el estado de los widgets con tu lógica y facilitar actualizaciones reactivas.
- **Callbacks sin paréntesis** 🔔: al asignar funciones a botones o menús usa `command=mi_funcion` (sin `()`), o `lambda` si necesitas parámetros.
- **Separación por marcos** 🧱: organiza la UI en `Frame`s para mantener el layout limpio y reutilizable.
- **Evita bloqueos** ⏳: no ejecutes tareas largas en el hilo principal; usa hilos o colas si necesitas procesos costosos.

## ✅ Resultado esperado

* Ventanas funcionales con textos e imágenes correctamente posicionados.
* Formularios que capturan y muestran datos del usuario.
* Diálogos de alerta que interactúan con el flujo de la app.
* Menús operativos para navegar o ejecutar acciones comunes.

---

👉 Con este bloque aprenderás los fundamentos para construir GUIs con Tkinter: desde el layout y los widgets básicos hasta interacciones y menús. Explora cada archivo en orden para afianzar los conceptos.


