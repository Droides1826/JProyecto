-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 10-02-2025 a las 23:32:03
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
  `nombre_categoria` varchar(255) DEFAULT NULL,
  `descripcion` text DEFAULT NULL,
  `estado` enum('activo','inactivo') NOT NULL DEFAULT 'activo'
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `categorias`
--

INSERT INTO `categorias` (`id_categoria`, `nombre_categoria`, `descripcion`, `estado`) VALUES
(1, 'Home', 'Todos los productos que necesitas', 'inactivo');

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

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pedidos`
--

CREATE TABLE `pedidos` (
  `id_pedido` int(11) NOT NULL,
  `fecha_pedido` datetime DEFAULT current_timestamp(),
  `estado` enum('pendiente','en proceso','enviado','cancelado') NOT NULL,
  `id_producto` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `precio_unitario` decimal(10,2) NOT NULL,
  `valor_total` decimal(10,2) GENERATED ALWAYS AS (`cantidad` * `precio_unitario`) STORED
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `pedidos`
--

INSERT INTO `pedidos` (`id_pedido`, `fecha_pedido`, `estado`, `id_producto`, `cantidad`, `precio_unitario`) VALUES
(10, '2025-02-10 17:04:02', 'pendiente', 2, 41, 22.00);

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
  `imagen` blob DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `productos`
--

INSERT INTO `productos` (`id_producto`, `nombre`, `descripcion`, `precio`, `estado`, `id_categoria`, `cantidad`, `imagen`) VALUES
(1, 'llaves', 'Nombre actualizado', 2500.00, 'activo', 1, 10, 0x70726f647563746f5f313733373733323731372e6a7067);

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
  ADD PRIMARY KEY (`id_pedido`),
  ADD KEY `id_producto` (`id_producto`);

--
-- Indices de la tabla `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`id_producto`),
  ADD KEY `id_categoria` (`id_categoria`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `categorias`
--
ALTER TABLE `categorias`
  MODIFY `id_categoria` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=100;

--
-- AUTO_INCREMENT de la tabla `historial_cambios`
--
ALTER TABLE `historial_cambios`
  MODIFY `id_cambio` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT de la tabla `historial_estados_pedido`
--
ALTER TABLE `historial_estados_pedido`
  MODIFY `id_cambio` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `pedidos`
--
ALTER TABLE `pedidos`
  MODIFY `id_pedido` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT de la tabla `productos`
--
ALTER TABLE `productos`
  MODIFY `id_producto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=44;

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
-- Filtros para la tabla `pedidos`
--
ALTER TABLE `pedidos`
  ADD CONSTRAINT `pedidos_ibfk_1` FOREIGN KEY (`id_producto`) REFERENCES `productos` (`id_producto`);

--
-- Filtros para la tabla `productos`
--
ALTER TABLE `productos`
  ADD CONSTRAINT `productos_ibfk_1` FOREIGN KEY (`id_categoria`) REFERENCES `categorias` (`id_categoria`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
