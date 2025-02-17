-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 17-02-2025 a las 23:26:02
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
  `estado` tinyint(1) NOT NULL DEFAULT 1 CHECK (`estado` in (1,2))
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `categorias`
--

INSERT INTO `categorias` (`id_categoria`, `nombre_categoria`, `descripcion`, `estado`) VALUES
(1, 'Hogar', 'Descubre una amplia variedad de productos diseñados para hacer tu casa más confortable, funcional y acogedora. Desde decoración y mobiliario hasta artículos de organización y limpieza, todo lo que necesitas para crear el ambiente perfecto en tu hogar.', 1),
(2, '2323', 'äa//', 1),
(3, '', 'äa//', 1),
(4, 'L', 'Elemento para lentes', 1);

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
(23, 45, 'nombre', 'llave', 'Camion', '2025-02-11 15:48:50'),
(24, 45, 'nombre', 'Camion', 'Camion 222', '2025-02-11 17:15:45'),
(25, 45, 'descripcion', 'llave de torque', 'camion de 15tn', '2025-02-11 17:16:38'),
(26, 45, 'precio', '1000.00', '0.00', '2025-02-11 17:16:58'),
(27, 45, 'precio', '0.00', '100.00', '2025-02-11 17:18:28'),
(28, 45, 'estado', 'activo', '', '2025-02-11 17:25:31'),
(29, 45, 'estado', '', 'activo', '2025-02-11 17:27:09'),
(30, 45, 'estado', 'activo', '', '2025-02-11 17:27:11'),
(31, 45, 'estado', '', 'activo', '2025-02-11 17:40:33'),
(32, 45, 'estado', 'activo', 'inactivo', '2025-02-11 17:43:28'),
(33, 45, 'estado', 'inactivo', 'activo', '2025-02-11 17:43:34'),
(34, 45, 'precio', '100.00', '1000.00', '2025-02-12 08:33:08'),
(35, 45, 'precio', '1000.00', '50000.00', '2025-02-12 08:34:16'),
(36, 45, 'precio', '50000.00', '500000.00', '2025-02-12 08:38:21'),
(37, 45, 'estado', '', '1', '2025-02-12 08:40:29'),
(38, 46, 'estado', '', '1', '2025-02-12 08:40:33'),
(39, 45, 'estado', '1', '2', '2025-02-12 08:51:30'),
(45, 45, 'estado', '2', '1', '2025-02-12 08:53:37'),
(46, 45, 'estado', '1', '2', '2025-02-12 08:54:11'),
(47, 45, 'estado', '2', '1', '2025-02-12 08:57:46'),
(48, 45, 'estado', '1', '2', '2025-02-12 08:59:06'),
(49, 45, 'precio', '500000.00', '122222.00', '2025-02-12 11:28:54'),
(50, 45, 'precio', '122222.00', '12222.00', '2025-02-12 11:29:59'),
(51, 45, 'nombre', 'Camion 222', '2222', '2025-02-12 14:14:05'),
(52, 45, 'nombre', '2222', 'Gorra', '2025-02-12 14:14:28'),
(53, 45, 'descripcion', 'camion de 15tn', 'Gorra', '2025-02-12 14:14:38'),
(54, 45, 'descripcion', 'Gorra', '22', '2025-02-12 14:15:03'),
(55, 45, 'estado', '2', '1', '2025-02-12 14:15:23'),
(56, 45, 'estado', '1', '2', '2025-02-12 14:17:49'),
(57, 55, 'descripcion', 'Cripi', 'Crispetas de queso', '2025-02-12 15:12:14'),
(58, 55, 'nombre', 'Crispeta', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', '2025-02-12 15:15:03'),
(59, 55, 'nombre', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'Crispetaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', '2025-02-12 15:15:35'),
(60, 55, 'nombre', 'Crispetaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'Crispeta', '2025-02-12 15:16:09'),
(61, 55, 'precio', '2000.00', '99999999.99', '2025-02-12 15:16:09'),
(62, 55, 'precio', '99999999.99', '200000000.00', '2025-02-12 15:18:16'),
(63, 55, 'estado', '1', '2', '2025-02-12 15:19:35'),
(64, 55, 'nombre', 'Crispeta', 'Crispetsssssssssssssssssssssssssssssssssssssssssssssssssa', '2025-02-12 15:22:37'),
(65, 55, 'nombre', 'Crispetsssssssssssssssssssssssssssssssssssssssssssssssssa', 'Crispetssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssa', '2025-02-12 15:22:42'),
(66, 55, 'nombre', 'Crispetssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssa', 'csdsadsadadadadddddddddddddddddddddddddddddddddddddddddddddddddddddddd', '2025-02-12 15:24:25'),
(67, 55, 'nombre', 'csdsadsadadadadddddddddddddddddddddddddddddddddddddddddddddddddddddddd', 'csdsadsadadadadddddddddddddddddddddddddddddddddddddddddddqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqddddddddddddd', '2025-02-12 15:33:21'),
(68, 55, 'nombre', 'csdsadsadadadadddddddddddddddddddddddddddddddddddddddddddqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqddddddddddddd', 'csdsqqqqqqqqqqqqqqaaaaaaaaaaaaaaaaaaaaaaassssssssssssssssssssssssssssaaaqqddd', '2025-02-12 15:44:53'),
(69, 55, 'nombre', 'csdsqqqqqqqqqqqqqqaaaaaaaaaaaaaaaaaaaaaaassssssssssssssssssssssssssssaaaqqddd', 'csdsqqasdsa12312313qqqqqqqqqqqqaaaaaaaaaaaaaaaaaaaaaaassssssssssssssssssssssssssssaaaqqddd', '2025-02-12 15:45:04'),
(70, 55, 'nombre', 'csdsqqasdsa12312313qqqqqqqqqqqqaaaaaaaaaaaaaaaaaaaaaaassssssssssssssssssssssssssssaaaqqddd', 'csdsssssssssssssssssaaaqqddd', '2025-02-12 15:52:06'),
(71, 55, 'precio', '200000000.00', '2000.00', '2025-02-12 15:52:06'),
(72, 55, 'nombre', 'csdsssssssssssssssssaaaqqddd', 'csd', '2025-02-12 15:54:14'),
(73, 55, 'precio', '2000.00', '0.00', '2025-02-12 15:59:16'),
(74, 55, 'precio', '0.00', '100.00', '2025-02-12 16:02:50'),
(75, 55, 'precio', '100.00', '100000.00', '2025-02-12 16:06:03'),
(76, 55, 'estado', '2', '1', '2025-02-12 16:33:01'),
(79, 55, 'estado', '1', '2', '2025-02-12 16:35:34'),
(80, 55, 'nombre', 'csd', 'ddadsafsdsadqqqqqqqqqqqqqqqq', '2025-02-12 16:48:42'),
(81, 55, 'descripcion', 'Crispetas de queso', 'Crispetas sddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddo', '2025-02-12 16:48:42'),
(82, 55, 'precio', '100000.00', '100000000.00', '2025-02-12 16:53:12'),
(83, 55, 'estado', '2', '1', '2025-02-13 09:39:54'),
(84, 55, 'nombre', 'ddadsafsdsadqqqqqqqqqqqqqqqq', 'Crispetas', '2025-02-13 10:27:15'),
(85, 55, 'precio', '100000000.00', '100000.00', '2025-02-13 10:27:40'),
(86, 55, 'precio', '100000.00', '10000.00', '2025-02-13 10:28:12'),
(87, 1, 'precio', '50000.00', '100000.00', '2025-02-13 10:48:09'),
(88, 1, 'precio', '100000.00', '1000.00', '2025-02-13 10:49:21'),
(89, 1, 'precio', '1000.00', '100.00', '2025-02-13 10:51:36'),
(90, 1, 'descripcion', 'Producto de limpieza del hogar, ', 'aaaa', '2025-02-13 10:53:05'),
(91, 1, 'descripcion', 'aaaa', 'Producto de limpieza del hogar,', '2025-02-13 10:53:14'),
(92, 1, 'nombre', 'trapeador', 'escoba', '2025-02-13 10:53:28'),
(93, 1, 'nombre', 'escoba', 'Trapeador aaa', '2025-02-13 10:53:37'),
(94, 1, 'nombre', 'Trapeador aaa', 'Trapeador', '2025-02-13 10:53:45'),
(95, 1, 'estado', '1', '2', '2025-02-13 10:54:20'),
(96, 1, 'estado', '2', '1', '2025-02-13 10:54:25'),
(97, 1, 'nombre', 'Trapeador', '1', '2025-02-13 14:49:57'),
(98, 1, 'nombre', '1', '2', '2025-02-13 14:50:57'),
(99, 1, 'descripcion', 'Producto de limpieza del hogar,', '1', '2025-02-13 14:51:36'),
(100, 1, 'precio', '100.00', '0.00', '2025-02-13 14:51:57'),
(101, 1, 'precio', '0.00', '1000.00', '2025-02-13 15:02:26'),
(102, 1, 'nombre', '2', 'Hola', '2025-02-13 15:06:00'),
(103, 1, 'descripcion', '1', 'speed max 2', '2025-02-13 15:08:45'),
(104, 1, 'nombre', 'Hola', 'Wd40', '2025-02-13 15:13:19'),
(105, 1, 'precio', '1000.00', '20000.00', '2025-02-13 15:13:19'),
(106, 1, 'nombre', 'Wd40', '4', '2025-02-13 15:13:31'),
(107, 1, 'nombre', '4', 'wd40', '2025-02-13 15:14:28'),
(108, 1, 'nombre', 'wd40', '444aaaaaa', '2025-02-13 15:14:38'),
(109, 1, 'nombre', '444aaaaaa', 'ola', '2025-02-13 15:15:00'),
(110, 1, 'precio', '20000.00', '4.00', '2025-02-13 15:15:00'),
(111, 3, 'nombre', 'Lente Bifocal', 'Lentes Transition', '2025-02-14 14:17:22'),
(112, 3, 'descripcion', 'Lente para 2 tipos de aumento', 'Lentes Especiales reactivos a la luz', '2025-02-14 14:17:22'),
(113, 3, 'precio', '100000.00', '500000.00', '2025-02-14 14:17:22');

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
  `id_producto` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `precio_unitario` double(10,2) NOT NULL,
  `valor_total` double(10,2) GENERATED ALWAYS AS (`cantidad` * `precio_unitario`) STORED,
  `estado` tinyint(1) NOT NULL DEFAULT 3 CHECK (`estado` in (3,4,5,6))
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `pedidos`
--

INSERT INTO `pedidos` (`id_pedido`, `fecha_pedido`, `id_producto`, `cantidad`, `precio_unitario`, `estado`) VALUES
(1, '2025-02-13 10:54:49', 1, 10, 100.00, 6),
(2, '2025-02-14 14:18:43', 3, 10, 500000.00, 3),
(3, '2025-02-14 14:21:23', 3, 5, 500000.00, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

CREATE TABLE `productos` (
  `id_producto` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `descripcion` text DEFAULT NULL,
  `precio` double(12,2) NOT NULL,
  `id_categoria` int(11) DEFAULT NULL,
  `cantidad` int(11) NOT NULL,
  `estado` tinyint(1) NOT NULL DEFAULT 1 CHECK (`estado` in (1,2))
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `productos`
--

INSERT INTO `productos` (`id_producto`, `nombre`, `descripcion`, `precio`, `id_categoria`, `cantidad`, `estado`) VALUES
(1, 'ola', 'speed max 2', 4.00, 1, 9999, 1),
(2, 'yuca', 'yuca e` finca', 10.00, 1, 1000, 1),
(3, 'Lentes Transition', 'Lentes Especiales reactivos a la luz', 500000.00, 4, 0, 1);

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
  MODIFY `id_categoria` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `historial_cambios`
--
ALTER TABLE `historial_cambios`
  MODIFY `id_cambio` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=114;

--
-- AUTO_INCREMENT de la tabla `historial_estados_pedido`
--
ALTER TABLE `historial_estados_pedido`
  MODIFY `id_cambio` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `pedidos`
--
ALTER TABLE `pedidos`
  MODIFY `id_pedido` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `productos`
--
ALTER TABLE `productos`
  MODIFY `id_producto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

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
