-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 28-01-2025 a las 17:48:01
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `pproyecto`
--
CREATE DATABASE IF NOT EXISTS `pproyecto` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `pproyecto`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categorias`
--

CREATE TABLE `categorias` (
  `id_categoria` int(11) NOT NULL,
  `nombre_categoria` varchar(255) NOT NULL,
  `descripcion` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `categorias`
--

INSERT INTO `categorias` (`id_categoria`, `nombre_categoria`, `descripcion`) VALUES
(1, 'Hogar', 'Productos para el hogar'),
(2, 'comida', 'Descubre nuestra variedad de productos esenciales para tu cocina. Ofrecemos arroz de calidad, aceites saludables y granos seleccionados, perfectos para preparar tus recetas favoritas.'),
(3, 'mascotas', 'Encuentra todo lo que necesitas para consentir a tu mascota con nuestra selección de productos diseñados para su comodidad y felicidad.'),
(4, 'vehiculos', 'Encuentra el vehículo ideal para tus necesidades con nuestra amplia selección de autos, camionetas y motocicletas.'),
(5, 'ferreteria', 'En nuestra ferretería encontrarás una amplia gama de herramientas, materiales y equipos para llevar a cabo cualquier proyecto, desde reparaciones básicas hasta grandes construcciones.');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `historial_cambios`
--

CREATE TABLE `historial_cambios` (
  `id_cambio` int(11) NOT NULL,
  `id_producto` int(11) DEFAULT NULL,
  `campo` varchar(50) DEFAULT NULL,
  `valor_antiguo` text DEFAULT NULL,
  `valor_nuevo` text DEFAULT NULL,
  `fecha_cambio` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `historial_cambios`
--

INSERT INTO `historial_cambios` (`id_cambio`, `id_producto`, `campo`, `valor_antiguo`, `valor_nuevo`, `fecha_cambio`) VALUES
(1, 1, 'precio', '250.00', '220.00', '2025-01-23 11:05:03');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `historial_estados_pedido`
--

CREATE TABLE `historial_estados_pedido` (
  `id_cambio` int(11) NOT NULL,
  `id_pedido` int(11) DEFAULT NULL,
  `estado_antiguo` enum('pendiente','en proceso','enviado','cancelado') DEFAULT NULL,
  `estado_nuevo` enum('pendiente','en proceso','enviado','cancelado') DEFAULT NULL,
  `fecha_cambio` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `historial_estados_pedido`
--

INSERT INTO `historial_estados_pedido` (`id_cambio`, `id_pedido`, `estado_antiguo`, `estado_nuevo`, `fecha_cambio`) VALUES
(1, 1, 'pendiente', 'enviado', '2025-01-23 11:07:10');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pedidos`
--

CREATE TABLE `pedidos` (
  `id_pedido` int(11) NOT NULL,
  `fecha_pedido` datetime DEFAULT current_timestamp(),
  `estado` enum('pendiente','en proceso','enviado','cancelado') NOT NULL,
  `valor_total` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `pedidos`
--

INSERT INTO `pedidos` (`id_pedido`, `fecha_pedido`, `estado`, `valor_total`) VALUES
(1, '2025-01-23 11:06:55', 'enviado', 300.00);

--
-- Disparadores `pedidos`
--
DELIMITER $$
CREATE TRIGGER `seguimiento_estado_pedido_before_update` BEFORE UPDATE ON `pedidos` FOR EACH ROW BEGIN
    IF OLD.estado != NEW.estado THEN
        INSERT INTO Historial_Estados_Pedido (id_pedido, estado_antiguo, estado_nuevo, fecha_cambio)
        VALUES (OLD.id_pedido, OLD.estado, NEW.estado, NOW());
    END IF;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

CREATE TABLE `productos` (
  `id_producto` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `descripcion` text DEFAULT NULL,
  `precio` decimal(10,2) NOT NULL,
  `estado` enum('activo','inactivo') NOT NULL,
  `id_categoria` int(11) DEFAULT NULL,
  `cantidad` int(11) NOT NULL,
  `nombre_imagen` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `productos`
--

INSERT INTO `productos` (`id_producto`, `nombre`, `descripcion`, `precio`, `estado`, `id_categoria`, `cantidad`, `nombre_imagen`) VALUES
(1, 'Sofá', 'Sofá de 3 plazas', 220.00, 'activo', 1, 10, 'producto_1737732717.jpg'),
(2, 'Producto 1', 'Descripción del Producto 1', 100.00, 'activo', 1, 10, 'producto_1737732717.jpg'),
(3, 'Producto 2', 'Descripción del Producto 2', 150.00, 'activo', 2, 20, 'producto_1737732717.jpg'),
(4, 'Producto 3', 'Descripción del Producto 3', 200.00, 'activo', 3, 20, 'producto_1737732717.jpg'),
(5, 'Producto 4', 'Descripción del Producto 4', 250.00, 'activo', 1, 15, 'producto_1737732717.jpg'),
(6, 'Producto 5', 'Descripción del Producto 5', 120.00, 'activo', 4, 30, 'producto_1737732717.jpg'),
(7, 'Producto 6', 'Descripción del Producto 6', 180.00, 'activo', 1, 25, 'producto_1737732717.jpg'),
(8, 'Producto 7', 'Descripción del Producto 7', 220.00, 'activo', 4, 40, 'producto_1737732717.jpg'),
(9, 'Producto 8', 'Descripción del Producto 8', 270.00, 'activo', 2, 50, 'producto_1737732717.jpg'),
(10, 'Producto 9', 'Descripción del Producto 9', 130.00, 'activo', 3, 35, 'producto_1737732717.jpg'),
(11, 'Producto 10', 'Descripción del Producto 10', 160.00, 'activo', 1, 60, 'producto_1737732717.jpg'),
(12, 'Producto 11', 'Descripción del Producto 11', 190.00, 'activo', 1, 15, 'producto_1737732717.jpg'),
(13, 'Producto 12', 'Descripción del Producto 12', 210.00, 'activo', 5, 20, 'producto_1737732717.jpg'),
(14, 'Producto 13', 'Descripción del Producto 13', 240.00, 'activo', 1, 45, 'producto_1737732717.jpg'),
(15, 'Producto 14', 'Descripción del Producto 14', 300.00, 'activo', 2, 30, 'producto_1737732717.jpg'),
(17, 'Agua', 'agua embotellada', 30000000.00, 'activo', 5, 2, 'producto_1737732717.jpg'),
(18, 'Agua', 'ojo', 30000.00, 'activo', 1, 100, 'producto_1737733329.jpg'),
(19, 'Agua', 'ojo', 30000.00, 'activo', 3, 100, 'producto_1737994263.jpg');

--
-- Disparadores `productos`
--
DELIMITER $$
CREATE TRIGGER `seguimiento_producto_before_update` BEFORE UPDATE ON `productos` FOR EACH ROW BEGIN
    IF OLD.nombre != NEW.nombre THEN
        INSERT INTO Historial_Cambios (id_producto, campo, valor_antiguo, valor_nuevo, fecha_cambio)
        VALUES (OLD.id_producto, 'nombre', OLD.nombre, NEW.nombre, NOW());
    END IF;

    IF OLD.descripcion != NEW.descripcion THEN
        INSERT INTO Historial_Cambios (id_producto, campo, valor_antiguo, valor_nuevo, fecha_cambio)
        VALUES (OLD.id_producto, 'descripcion', OLD.descripcion, NEW.descripcion, NOW());
    END IF;

    IF OLD.precio != NEW.precio THEN
        INSERT INTO Historial_Cambios (id_producto, campo, valor_antiguo, valor_nuevo, fecha_cambio)
        VALUES (OLD.id_producto, 'precio', OLD.precio, NEW.precio, NOW());
    END IF;

    IF OLD.estado != NEW.estado THEN
        INSERT INTO Historial_Cambios (id_producto, campo, valor_antiguo, valor_nuevo, fecha_cambio)
        VALUES (OLD.id_producto, 'estado', OLD.estado, NEW.estado, NOW());
    END IF;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos_pedido`
--

CREATE TABLE `productos_pedido` (
  `id_pedido` int(11) NOT NULL,
  `id_producto` int(11) NOT NULL,
  `cantidad` int(11) DEFAULT NULL,
  `precio_unitario` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `productos_pedido`
--

INSERT INTO `productos_pedido` (`id_pedido`, `id_producto`, `cantidad`, `precio_unitario`) VALUES
(1, 1, 1, 250.00);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `categorias`
--
ALTER TABLE `categorias`
  ADD PRIMARY KEY (`id_categoria`);

--
-- Indices de la tabla `historial_cambios`
--
ALTER TABLE `historial_cambios`
  ADD PRIMARY KEY (`id_cambio`),
  ADD KEY `id_producto` (`id_producto`);

--
-- Indices de la tabla `historial_estados_pedido`
--
ALTER TABLE `historial_estados_pedido`
  ADD PRIMARY KEY (`id_cambio`),
  ADD KEY `id_pedido` (`id_pedido`);

--
-- Indices de la tabla `pedidos`
--
ALTER TABLE `pedidos`
  ADD PRIMARY KEY (`id_pedido`);

--
-- Indices de la tabla `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`id_producto`),
  ADD KEY `id_categoria` (`id_categoria`);

--
-- Indices de la tabla `productos_pedido`
--
ALTER TABLE `productos_pedido`
  ADD PRIMARY KEY (`id_pedido`,`id_producto`),
  ADD KEY `id_producto` (`id_producto`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `categorias`
--
ALTER TABLE `categorias`
  MODIFY `id_categoria` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `historial_cambios`
--
ALTER TABLE `historial_cambios`
  MODIFY `id_cambio` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `historial_estados_pedido`
--
ALTER TABLE `historial_estados_pedido`
  MODIFY `id_cambio` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `pedidos`
--
ALTER TABLE `pedidos`
  MODIFY `id_pedido` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `productos`
--
ALTER TABLE `productos`
  MODIFY `id_producto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `historial_cambios`
--
ALTER TABLE `historial_cambios`
  ADD CONSTRAINT `historial_cambios_ibfk_1` FOREIGN KEY (`id_producto`) REFERENCES `productos` (`id_producto`);

--
-- Filtros para la tabla `historial_estados_pedido`
--
ALTER TABLE `historial_estados_pedido`
  ADD CONSTRAINT `historial_estados_pedido_ibfk_1` FOREIGN KEY (`id_pedido`) REFERENCES `pedidos` (`id_pedido`);

--
-- Filtros para la tabla `productos`
--
ALTER TABLE `productos`
  ADD CONSTRAINT `productos_ibfk_1` FOREIGN KEY (`id_categoria`) REFERENCES `categorias` (`id_categoria`);

--
-- Filtros para la tabla `productos_pedido`
--
ALTER TABLE `productos_pedido`
  ADD CONSTRAINT `productos_pedido_ibfk_1` FOREIGN KEY (`id_pedido`) REFERENCES `pedidos` (`id_pedido`),
  ADD CONSTRAINT `productos_pedido_ibfk_2` FOREIGN KEY (`id_producto`) REFERENCES `productos` (`id_producto`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
