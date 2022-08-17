-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 11-08-2022 a las 21:15:43
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `Dataclasses`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `student`
--

CREATE TABLE `student` (
  `id` int(11) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `lname` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `age` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `student`
--

INSERT INTO `student` (`id`, `name`, `lname`, `email`, `age`) VALUES
(1, 'Kore', 'Gallamore', 'kgallamore0@uiuc.edu', 38),
(2, 'Normy', 'Leyzell', 'nleyzell1@ihg.com', 41),
(3, 'Ambrosio', 'Vause', 'avause2@scribd.com', 17),
(4, 'Angelika', 'Innott', 'ainnott3@bandcamp.com', 46),
(5, 'Gabriella', 'Fine', 'gfine4@slate.com', 49),
(6, 'Cordy', 'Matei', 'cmatei5@blogger.com', 70),
(7, 'Ody', 'MacKartan', 'omackartan6@imgur.com', 83),
(8, 'Johnny', 'Sugar', 'jsugar7@cocolog-nifty.com', 48),
(9, 'Michaeline', 'Redman', 'mredman8@sphinn.com', 3),
(10, 'Gail', 'Biagi', 'gbiagi9@smugmug.com', 92),
(11, 'Shaine', 'Maybery', 'smayberya@delicious.com', 91),
(12, 'Moria', 'Cristoforo', 'mcristoforob@lycos.com', 62),
(13, 'Townsend', 'Likely', 'tlikelyc@hubpages.com', 8),
(14, 'Den', 'Baxster', 'dbaxsterd@phpbb.com', 10),
(15, 'Jennette', 'Sansun', 'jsansune@php.net', 83),
(16, 'Val', 'Beckett', 'vbeckettf@businessweek.com', 78),
(17, 'Hadria', 'Carberry', 'hcarberryg@examiner.com', 79),
(18, 'Rochester', 'Dulake', 'rdulakeh@tamu.edu', 62),
(19, 'Randie', 'Brandrick', 'rbrandricki@hibu.com', 44),
(20, 'Ben', 'Brasner', 'bbrasnerj@nasa.gov', 91),
(21, 'Tiler', 'Woodwing', 'twoodwingk@barnesandnoble.com', 19),
(22, 'Una', 'De Pietri', 'udepietril@posterous.com', 71),
(23, 'Bink', 'Roseveare', 'brosevearem@mtv.com', 45),
(24, 'Katie', 'Pearcehouse', 'kpearcehousen@blogspot.com', 11),
(25, 'Sterne', 'Mogridge', 'smogridgeo@ibm.com', 91),
(26, 'Bernete', 'Pellatt', 'bpellattp@illinois.edu', 5),
(27, 'Fabien', 'MacAlpyne', 'fmacalpyneq@dagondesign.com', 3),
(28, 'Worden', 'Holttom', 'wholttomr@surveymonkey.com', 94),
(29, 'Ebeneser', 'Dimberline', 'edimberlines@nymag.com', 63),
(30, 'Annalise', 'MacDiarmid', 'amacdiarmidt@shareasale.com', 27),
(31, 'Meridel', 'Bowie', 'mbowieu@howstuffworks.com', 14),
(32, 'Arnie', 'Kasting', 'akastingv@artisteer.com', 59),
(33, 'Elianore', 'Klazenga', 'eklazengaw@slideshare.net', 7),
(34, 'Vernen', 'Stearns', 'vstearnsx@addtoany.com', 40),
(35, 'Bald', 'Lackner', 'blacknery@java.com', 22),
(36, 'Warde', 'Lashmore', 'wlashmorez@squidoo.com', 7),
(37, 'Brittani', 'Marsham', 'bmarsham10@clickbank.net', 19),
(38, 'Doralynne', 'Curzey', 'dcurzey11@phpbb.com', 3),
(39, 'Carce', 'Haslam', 'chaslam12@yellowpages.com', 34),
(40, 'Crichton', 'Jandak', 'cjandak13@i2i.jp', 28),
(41, 'Heindrick', 'Fantham', 'hfantham14@github.io', 17),
(42, 'Krystal', 'Henrion', 'khenrion15@wp.com', 26),
(43, 'Bryn', 'Smewings', 'bsmewings16@dropbox.com', 68),
(44, 'Orelle', 'Skinner', 'oskinner17@mlb.com', 34),
(45, 'Loraine', 'Suche', 'lsuche18@salon.com', 91),
(46, 'Storm', 'Schorah', 'sschorah19@blogs.com', 35),
(47, 'Yank', 'Skillman', 'yskillman1a@google.cn', 34),
(48, 'Fanchon', 'Turle', 'fturle1b@cmu.edu', 53),
(49, 'Teador', 'Willbraham', 'twillbraham1c@drupal.org', 20),
(50, 'Meghann', 'Ravenscroft', 'mravenscroft1d@paypal.com', 2),
(51, 'Shadow', 'Schutter', 'sschutter1e@ucoz.ru', 91),
(52, 'Brand', 'Yuill', 'byuill1f@unblog.fr', 36),
(53, 'Sigismondo', 'Josilowski', 'sjosilowski1g@omniture.com', 14),
(54, 'Rosemonde', 'Brumble', 'rbrumble1h@mtv.com', 72),
(55, 'Erny', 'Ivanichev', 'eivanichev1i@trellian.com', 87),
(56, 'Marylou', 'Merman', 'mmerman1j@prweb.com', 71),
(57, 'Arne', 'Listone', 'alistone1k@dmoz.org', 79),
(58, 'Alanson', 'Atty', 'aatty1l@smh.com.au', 45),
(59, 'Albina', 'Chapling', 'achapling1m@blogtalkradio.com', 66),
(60, 'Blaine', 'LLelweln', 'bllelweln1n@livejournal.com', 40),
(61, 'Hamlen', 'Rymell', 'hrymell1o@ucla.edu', 57),
(62, 'Mercy', 'Jelley', 'mjelley1p@about.com', 100),
(63, 'Frans', 'Qualtro', 'fqualtro1q@umich.edu', 23),
(64, 'Juliet', 'Gallyhaock', 'jgallyhaock1r@spotify.com', 37),
(65, 'Chloette', 'Blemings', 'cblemings1s@quantcast.com', 43),
(66, 'Loria', 'Brayley', 'lbrayley1t@cloudflare.com', 33),
(67, 'Kendal', 'Bonny', 'kbonny1u@nasa.gov', 46),
(68, 'Shandy', 'Adamowicz', 'sadamowicz1v@flavors.me', 16),
(69, 'Jorge', 'Swendell', 'jswendell1w@sohu.com', 5),
(70, 'Kippie', 'Turneaux', 'kturneaux1x@addtoany.com', 89),
(71, 'Mozes', 'Khomin', 'mkhomin1y@networksolutions.com', 66),
(72, 'Jobyna', 'Sedcole', 'jsedcole1z@tumblr.com', 73),
(73, 'Darn', 'Gouldeby', 'dgouldeby20@seattletimes.com', 63),
(74, 'Alonso', 'Dimitriou', 'adimitriou21@vimeo.com', 75),
(75, 'Erda', 'Menary', 'emenary22@msu.edu', 46),
(76, 'Jocko', 'Woolham', 'jwoolham23@ft.com', 3),
(77, 'Burg', 'Patrick', 'bpatrick24@google.com.hk', 2),
(78, 'Wayland', 'Mewrcik', 'wmewrcik25@berkeley.edu', 28),
(79, 'Enoch', 'Bourrel', 'ebourrel26@independent.co.uk', 63),
(80, 'Abra', 'Devey', 'aodevey27@chronoengine.com', 3),
(81, 'Patience', 'Whitehorne', 'pwhitehorne28@people.com.cn', 63),
(82, 'Marianna', 'Eriksson', 'meriksson29@cbc.ca', 70),
(83, 'Valentia', 'Gunton', 'vgunton2a@uol.com.br', 71),
(84, 'Sebastiano', 'Smaleman', 'ssmaleman2b@imageshack.us', 98),
(85, 'Blake', 'Brazel', 'bbrazel2c@discovery.com', 71),
(86, 'Coretta', 'Dmitrichenko', 'cdmitrichenko2d@jimdo.com', 83),
(87, 'Sigrid', 'Hann', 'shann2e@whitehouse.gov', 31),
(88, 'Ileana', 'Flisher', 'iflisher2f@nationalgeographic.com', 89),
(89, 'Jody', 'Sends', 'jsends2g@si.edu', 43),
(90, 'Brose', 'Dameisele', 'bdameisele2h@sakura.ne.jp', 96),
(91, 'Chelsy', 'Shortan', 'cshortan2i@archive.org', 29),
(92, 'Ryon', 'Ivanishin', 'rivanishin2j@indiegogo.com', 46),
(93, 'Zak', 'Doog', 'zdoog2k@google.es', 77),
(94, 'Desirae', 'Lyman', 'dlyman2l@slashdot.org', 19),
(95, 'Cristin', 'Habens', 'chabens2m@apache.org', 46),
(96, 'Ly', 'Boddington', 'lboddington2n@com.com', 14),
(97, 'Coleen', 'Gonet', 'cgonet2o@shutterfly.com', 34),
(98, 'Claudine', 'Baggs', 'cbaggs2p@wix.com', 70),
(99, 'Roi', 'Dearsley', 'rdearsley2q@engadget.com', 20),
(100, 'Marci', 'Worner', 'mworner2r@istockphoto.com', 98);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
