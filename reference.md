# **ABSTRACT**

The scarcity of clean water resources around the globe has generated a need for their optimum utilization. Internet of Things (IoT) solutions, based on the application-specific sensors’ data acquisition and intelligent processing, are bridging the gaps between the cyber and physical worlds. IoT-based smart irrigation management systems can help in achieving optimum water-resource utilization in the precision farming landscape. This paper presents an open-source technology-based smart system to predict the irrigation requirements of a field using the sensing of ground parameters like soil moisture, soil temperature, and environmental conditions along with the weather forecast data from the Internet. The sensing nodes, involved in the ground and environmental sensing, consider soil moisture, soil temperature, air temperature, Ultraviolet (UV) light radiation, and relative humidity of the crop field. The intelligence of the proposed system is based on a smart algorithm, which considers sensed data along with the weather forecast parameters like precipitation, air temperature, humidity, and UV for the near future. The complete system has been developed and deployed on a pilot scale, where the sensor node data is wirelessly collected over the cloud using web services, and a web-based information visualization and decision support system provides the real-time information insights based on the analysis of sensors data and weather forecast data. The system has a provision for closed-loop control of the water supply to realize a fully autonomous irrigation scheme. The paper describes the system and discusses in detail the information processing results of three weeks' data based on the proposed algorithm. The system is fully functional and the prediction results are very encouraging. The proposed system can be further enhanced with real-time soil water content-based soil moisture sensing, which will improve the accuracy of the irrigation demand prediction.

# **Introduction**

The scarcity of clean water resources around the globe has generated a need for their optimum utilization. The world is facing a water crisis, and it is predicted that by 2025, more than half of the world's population will be living in areas of high water stress. The irrigation is one of the most important water-conservation techniques that can be used to reduce the amount of water that is lost to evaporation and to increase the amount of water that is available for consumption. The irrigation systems are designed to deliver water to the crops at a rate that is sufficient to meet the crop's water requirements. The irrigation systems are designed to deliver water to the crops at a rate that is sufficient to meet the crop's water requirements. Irrigation scheduling is a complex task that requires a large amount of time and resources to complete. Irrigation scheduling is a complex task that requires a large amount of time and resources to complete. The irrigation scheduling is a complex task that requires a large amount of time and resources to complete.

The precipitation and evaporation are important key factors, which influence the soil moisture. In geography and climatology, the wetness of soil is estimated by the proportion of annual (or monthly) precipitation and evaporation (Shang et al., 2007). Daily soil moisture can also be evaluated by the ratio of daily precipitation and evaporation in the above perspective. Precipitation is directly accessible in the routine weather reports; nonetheless, evaporation can be calculated using other metrological essentials. For evaporation, we use an empirical model given by Penman (Chen and Chen, 1993)
$$
E_{T} \propto (E_{h}+E_{m})
$$
The total evaporation $ E_T$ depends on the heat evaporation $E_h$ and the dynamic evaporation $E_m$ , where $E_m$ depends upon the velocity of the land storm, air temperature, relative humidity of the air and UV radiation.

To achieve water saving, irrigation system frameworks have been proposed based on various techniques, e.g., thermal imaging, Crop Water Stress Index (CWSI), direct soil water measurements, etc. Thermal imaging is a prominent technique for irrigation management and it is based on the shade temperature distribution of the plant. In this framework, the status of the water in the plant is checked over continuous intervals and irrigation is planned in view of the shade temperature distribution of the plant (Wang et al., 2010). In addition, CWSI based framework has been proposed for irrigation scheduling of the crops for efficient use of water. The observation of CWSI was first characterized more than 30 years ago (O’Shaughnessy and Evett (2010) proposed an automatic irrigation scheduling based on direct soil water measurement that utilizes water proficiently over manual irrigation system. Allen et al. (1998) suggested evapotranspiration (ET) based approach, which is an important parameter to decide crop irrigation needs influenced by climate parameters, e.g., solar radiation, relative humidity, temperature, wind velocity, and crop features such as phase of the crop growth, assortment and plant density, properties of soil, nuisance, and disease control. ET-based frameworks can save water up to 42% over time-based water irrigation scheduling (Davis and Dukes, 2010). Davis et al. (2009) conducted the investigations in Florida and verified that ET‐based watering scheduling controllers are more beneficial in term of cost, size and labor requirement for irrigation. ET-based irrigation system uses much less water as compared to scheduled practices. Viani et al. (2017) proposed a fuzzy logic-based decision support system based on farmer’s experience with the understanding of crop condition. This system provides more water saving over single-threshold and multi-threshold based irrigation scheduling. Gutiérrez et al. (2014) proposed an automated irrigation system using a wireless sensor network and GPRS module to save water in irrigation. In this system, a network of soil moisture sensors with controller has been installed in a crop field for real-time monitoring and irrigation control. Gill et al. (2006) suggested a method for soil moisture prediction using support vector machines based on air temperature, relative air humidity and soil temperature. (Jaguey et al. (2015) developed irrigation sensor based on smart phone. For sensing soil moisture, the digital camera of smart phone is used to process RGB to gray for estimation of ratio between wet and dry area of soil. The ratio of wetness and dryness is transmitted via gateway to water motor controller. A Mobile Application (APP) is developed to control sensor activity (like wakeup) and to set sensor in sleep mode. Goldstein et al. (2017) proposed irrigation recommendations based on machine learning algorithm with support of agronomist’s encysted knowledge. It was found that the best regression model was Gradient Boosted Regression Trees (GBRT) with 93% accuracy in prediction of irrigation plan/recommendation. The developed model is helpful to the agronomist’s irrigation management. Roopaei et al. (2017) proposed an intelligent irrigation monitoring system based on thermal imaging. The proposed technique uses thermal imaging camera mounted on Drone. An algorithm is developed using images processing techniques for identification of water requirement, Leaf water potential, and nonuniform irrigation, which are used for irrigation monitoring. Majority of the earlier irrigation systems do not consider the weather forecasting information (e.g., precipitation) while making irrigation decisions. It leads to a wastage of fresh water, energy and loss of crop growth (due to excess water) when a rain is followed immediately by the watering of the crop. To handle such cases, IoT based solutions can provide a better decision support for irrigation by utilizing weather forecasting information (e.g., precipitation) from the Internet. Further, the accuracy of weather forecasting is improving due to the advancement of satellite imagery technology. For effective and optimum utilization of fresh water in irrigation, it becomes essential to develop the smart irrigation systems based on dynamic prediction of soil moisture pattern of the field and precipitation information of upcoming days. This paper presents an intelligent system that predicts soil moisture based on the information collected from the sensors deployed at the field and the weather forecast information available on the Internet. The field data has been collected through a self-designed sensor node. The server-side software has been developed with node side connectivity along with information visualization and decision support features. A novel algorithm has been developed for soil-moisture prediction, which is based on Machine Learning techniques applied on the sensor node data and the weather forecast data. The algorithm shows improved accuracy and less error. The proposed approach could help in making effective irrigation decisions with optimum water usage

# Related Work

## Evaporation

Prediction of soil moisture is vital for effective irrigation management system. The estimation of soil moisture depends upon evapotranspiration Hargreaves and Samani (1985) developed a method based on temperature and extra-terrestrial radiation to estimate $E_{T_0}$. It is expressed as
$$
E_{T_0}= 0.0023R_a(\frac{t_{max}+t_{min}}{2}+17.8) \sqrt{T_{max}-T_{min}}
$$
where where $E_{T_0}$ = reference evapotranspiration (mm/day); $T_{max}$ and $T_{min}$ = maximum temperature and minimum temperature (°C) and $R_a$ = extra-terrestrial radiation $(MJ m^{−2} day^{−1})$.

Ritchie developed another method for estimation of $E_{T_0}$ (Jones and Ritchie, 1990) based on temperature and solar radiation. It is expressed as
$$
E_{T_0}  = \alpha_{1}[3.87\times 10^{-3}\times R_s(0.6T_{max}+0.4T_{min}+29)]
$$
where $E_{T_{0}}$= reference evapotranspiration (mm/day); a$T_{max}$ and $T_{min}$ = maximum temperature and minimum temperature (°C) and $R_s$ = solar radiation $(MJ m^{−2} day^{−1})$. When
$$
\begin{cases}
      5<T_{max}\leq 35 ^{\circ} C & \alpha_1=1.1\\
      T_{max}>35 ^{\circ} C & \alpha_1=1.1+0.05(T_{max}-35)\\
      T_{max}<5^{\circ} C & \alpha_1=0.01\exp[0.18(T_{max}+20)]
    \end{cases}
$$
Cobaner (2011) developed evapotranspiration estimation method based on Neuro-Fuzzy (NF) inference and found that the NF model (based on solar radiation, air temperature, and relative humidity) exhibits better accuracy than the combination of solar radiation, air temperature and wind speed.From state of art, it has been analyzed that prediction of soil moisture is possible using sensors placement at the field and weather forecasted data. So, we have considered evaporation of soil moisture based on air temperature, air relative humidity, soil temperature, and radiation. The parameters are considered for analyzing the soil moisture drain (change/ difference) pattern based on the recorded data of soil moisture. An IoT based architecture (Fig. 1) has been proposed to collect, transmit and process the physical parameters (soil moisture, air temperature, air relative humidity, soil temperature, and radiation) of farming land along with the weather forecast information to manage the irrigation efficiently. An algorithm based on a combination of supervised and unsupervised machine learning techniques (block diagram shown in Fig. 3 and pseudocode is discussed in Section 3.2.1) has been developed using Support Vector Regression (SVR) and k-means clustering for estimation of difference/change in soil moisture due to weather conditions. It gives good accuracy and less Mean Squared Error (MSE) (Theobald, 1974; “Mean Squared Error, 2018’’) in the prediction of the soil moisture of upcoming days with the help of sensors data and the weather forecasting data. SVR model has been trained using data (air temperature, air relative humidity, soil temperature, radiation, and soil moisture difference) collected from field

# Proposed Work

## Time

to compensate for the loss of water due to evaporation, the Irrigation time must be compensated as well
$$
\tau_{t} = \tau_{o}+ \tau_{c}
$$
where $\tau_{t}$ is total time after compensation, $\tau_{o}$ time without compensation,$\tau_{c}$ comensated time
$$
\tau_{c}=\frac{E_{T_0}}{\text{Flow rate}}
$$

using this 
$$
\text{Flow rate}=\frac {H\times Area}{\tau_{o}}
$$

$$
\tau_{c}=\frac{E_{T_0}\tau_{o}}{H}
$$

$$
\tau_{t}=\tau_{o}\left(\frac{H+E_{T_0}}{H}\right)
$$

where $H$ is the required irrigation level  S

## Architecture/Model

```
                  ┌───────web-server────────┐
   ┌───────┐      │                         │
   │ input ├───┬──┼────┐  ┌────────┐        │
   └───────┘   │  │    └──► get_ev │        │                   ┌──────────────┐
               │  │       └───┬────┘ ┌──────┼───────────────────┤    Relay     │
 ┌─────────────┤  │           │      │      │                   ├──────────────┤
 │ open-weather│  │       ┌───┴────┐ │      │                   │┼┼┼┼┼┼┼┼┼┼┼┼┼┼│
 │     api     │  │       │get_time├─┘      │                   ├──────────────┤
 └─────────────┘  │       └────────┘        ├───────────────────┤              │
                  │                         │                   │ rassberry-pi │
                  └─────────────────────────┘                   │              │
                                                                └──────────────┘
```

![](C:\Users\swara\Desktop\Coding Shit\mitwpu-hack\Assets\arch-diagram.png)

## Software

**we get solar radiance from https://openweathermap.org/api/solar-radiation**

**we get daily temperature from https://openweathermap.org/api**

## Hardware

<img src="https://www.raspberrypi-spy.co.uk/wp-content/uploads/2012/06/Raspberry-Pi-GPIO-Header-with-Photo.png" alt="Simple Guide to the Raspberry Pi GPIO Header - Raspberry Pi Spy" style="zoom: 50%;" />

<img src="C:\Users\swara\Desktop\College Shit\Trimester VII\ES-IOT\mini\python.png" alt="python" style="zoom:50%;" />

<img src="https://components101.com/sites/default/files/inline-images/Single-Channel-Relay-Module-Circuit.png" alt="5V Single-Channel Relay Module - Pin Diagram, Specifications, Applications,  Working" style="zoom: 67%;" />

# Output

<img src="C:\Users\swara\AppData\Roaming\Typora\typora-user-images\image-20211005092731340.png" alt="image-20211005092731340" style="zoom:200%;" />

# Conclusion

The soil moisture is a critical parameter for developing a smart irrigation system. The soil moisture is affected by a number of environmental variables, e.g., air temperature, air humidity, UV, soil temperature, etc. With advancement in technologies, the weather forecasting accuracy has improved significantly and the weather forecasted data can be used for prediction of changes in the soil moisture. This project proposes an IoT based smart irrigation architecture along with a hybrid machine learning based approach to predict the soil moisture. The proposed algorithm data of recent past and the weather forecasted data for prediction of soil moisture of upcoming days. The predicted value of the soil moisture is better in terms of their accuracy and error rate. Further, the prediction approach is integrated into a standalone system prototype. The system prototype is cost effective, as it is based on the open standard technologies. The auto mode makes it a smart system and it can be further customized for application specific scenarios. In future, we are planning to conduct a water saving analysis based on proposed algorithm with multiple nodes along with minimizing the system cost.

# References

Allen, R.G., Pereira, L.S., Raes, D., Smith, M., Ab, W., 1998. Crop evapotranspiration -
guidelines for computing crop water requirements. FAO - Food Agric. Organ. United
Nations Rome 1–15. https://doi.org/10.1016/j.eja.2010.12.001.
API Reference [WWW Document], 2017. AccuWeather APIs (accessed 9.2.17). https://
developer.accuweather.com/accuweather-forecast-api/apis.
Chen, Q., Chen, T.Y., 1993. Estimation of river basin evapotranspi- ration over complex
terrain using NOAA AVHRR data. Acta Geogr. Sin. 48 (1), 61–69.
Cobaner, M., 2011. Evapotranspiration estimation by two different neuro-fuzzy inference
systems. J. Hydrol. 398, 292–302. https://doi.org/10.1016/j.jhydrol.2010.12.030.
da Cruz, M.A.A., Rodrigues, J.J.P.C., Al-Muhtadi, J., Korotaev, V., Albuquerque, V.H.C.,

A reference model for internet of things middleware. 1 1. IEEE Internet Things
J. 5. https://doi.org/10.1109/JIOT.2018.2796561.
Davis, S.L., Dukes, M.D., 2010. Irrigation scheduling performance by evapotranspirationbased controllers. Agric. Water Manage. 98, 19–28. https://doi.org/10.1016/j.agwat.
2010.07.006.
Davis, S.L., Dukes, M.D., Miller, G.L., 2009. Landscape irrigation by evapotranspirationbased irrigation controllers under dry conditions in Southwest Florida. Agric. Water
Manage. 96, 1828–1836. https://doi.org/10.1016/j.agwat.2009.08.005.
Drucker, H., Burges, C.J., Kaufman, L., Smola, A., Vapoik, V., 1997. Support vector regression machines. Adv. Neural Inf. Process. Syst. 1, 155–161. https://doi.org/10.1.1.
10.4845.
G. o. I. NITI Aayog, 2015. Raising Agricultural Productivity and Making Farming
Remunerative for Farmers [WWW Document] http://niti.gov.in/content/raisingagricultural-productivity-and-making-farming-remunerative-farmers (accessed 9.10.18).
Hargreaves, George H., Samani, Zohrab A., 1985. Reference crop evapotranspiration from
temperature. Appl. Eng. Agric. 1, 96–99. https://doi.org/10.13031/2013.26773.
Gill, M.K., Asefa, T., Kemblowski, M.W., McKee, M., 2006. Soil moisture prediction using
support vector machines. J. Am. Water Resour. Assoc. 42, 1033–1046. https://doi.
org/10.1111/j.1752-1688.2006.tb04512.x.
Goldstein, A., Fink, L., Meitin, A., Bohadana, S., Lutenberg, O., Ravid, G., 2017. Applying
machine learning on sensor data for irrigation recommendations: revealing the
agronomist’s tacit knowledge. Precis. Agric. 19, 421–444. https://doi.org/10.1007/
s11119-017-9527-4.
Gubbi, J., Buyya, R., Marusic, S., Palaniswami, M., 2013. Internet of things (IoT): a vision,
architectural elements, and future directions. Futur. Gener. Comput. Syst. 29,
1645–1660. https://doi.org/10.1016/j.future.2013.01.010.
Gutiérrez, J., Villa-medina, J.F., Nieto-Garibay, A., Porta-gándara, M.Á., Gutierrez, J.,
Villa-medina, J.F., Nieto-Garibay, A., Porta-Gandara, M.A., 2014. Automated irrigation system using a wireless sensor network and GPRS module. IEEE Trans. Instrum.
Meas. 63, 166–176. https://doi.org/10.1109/TIM.2013.2276487.
Hearst, M.A., Dumais, S.T., Osuna, E., Platt, J., Scholkopf, B., 1998. Support vector machines. IEEE Intell. Syst. Appl. 13, 18–28. https://doi.org/10.1109/5254.708428.
Idso, S.B., Jackson, R.D., Pinter, P.J., Reginato, R.J., Hatfield, J.L., 1981. Normalizing the
stress-degree-day parameter for environmental variability. Agric. Meteorol. 24,
45–55. https://doi.org/10.1016/0002-1571(81)90032-7.
Jaguey, J.G., Villa-Medina, J.F., Lopez-Guzman, A., Porta-Gandara, M.A., 2015.
Smartphone irrigation sensor. IEEE Sens. J. 15, 5122–5127. https://doi.org/10.
1109/JSEN.2015.2435516.
Jones, J.W., Ritchie, J.T., 1990. Crop growth models. In: Hoffman, G.J., Howel, T.A.,
Solomon, K.H. (Eds.), Management of Farm Irrigation System ASAE, pp. 63–89.
Shang, K.Z., Wang, S.G., Ma, Y.X., Zhou, Z.J., Wang, J.Y., Liu, H.L.Y., 2007. A scheme for
calculating soil moisture content by using routine weather data. Atmos. Chem. Phys.
7, 5197–5206. https://doi.org/10.1017/CBO9781107415324.004.
Kanungo, T., Mount, D.M., Netanyahu, N.S., Piatko, C.D., Silverman, R., Wu, A.Y., 2002. An
efficient k-means clustering algorithm: analysis and implementation. IEEE Trans. Pattern
Anal. Mach. Intell. 24, 881–892. https://doi.org/10.1109/TPAMI.2002.1017616.
Mean Squared Error [WWW Document], 2018. Tutorvista (accessed 8.29.18). https://
math.tutorvista.com/statistics/mean-squared-error.html.
O’Shaughnessy, S.A., Evett, S.R., 2010. Canopy temperature based system effectively
schedules and controls center pivot irrigation of cotton. Agric. Water Manage. 97,
1310–1316. https://doi.org/10.1016/j.agwat.2010.03.012.
Ojha, T., Misra, S., Raghuwanshi, N.S., 2015. Wireless sensor networks for agriculture: the
state-of-the-art in practice and future challenges. Comput. Electron. Agric. 118,
66–84. https://doi.org/10.1016/j.compag.2015.08.011.
Pandey, V.S., Sharma, D., Shukla, A.K., Tyagi, S., 2017. A low-cost zigbee based temperature and humidity acquisition system for research and industrial applications. In:
Dutta, C.R.K.S.D.K. (Ed.), International Conference on Communication Computing
and Networking, pp. 379–385.
Roopaei, M., Rad, P., Choo, K.R., Choo, R., 2017. Cloud of things in smart agriculture:
intelligent irrigation monitoring by thermal imaging. IEEE Cloud Comput. 4, 10–15.
Sharma, D., Shukla, A.K., Bhondekar, A.P., Ghanshyam, C., Ojha, A., 2016. A technical
assessment of IOT for Indian agriculture sector. In: IJCA Proc. Natl. Symp. Mod. Inf.
Commun. Technol Digit. Indiapp. 1–5.
Theobald, C.M., 1974. Generalizations of mean square error applied to ridge regression. J.
R. Stat. Soc. Ser. B 36, 103–106. https://doi.org/10.2307/2984775.
United Nations, 2013. World population projected to reach 9.6 billion by 2050 [WWW
Document]. Dep. Econ. Soc. Aff. Popul. Div. United Nations (accessed 2.12.18).
http://www.un.org/en/development/desa/news/population/un-report-worldpopulation-projected-to-reach-9-6-billion-by-2050.html.
Viani, F., Bertolli, M., Salucci, M., Polo, A., 2017. Low-cost wireless monitoring and decision support for water saving in agriculture. IEEE Sens. J. 17, 4299–4309. https://
doi.org/10.1109/JSEN.2017.2705043.
Wang, X., Yang, W., Wheaton, A., Cooley, N., Moran, B., 2010. Efficient registration of
optical and IR images for automatic plant water stress assessment. Comput. Electron.
Agric. 74, 230–237. https://doi.org/10.1016/j.compag.2010.08.004.
Weather API [WWW Document], 2012. Openweather (accessed 8.30.17). https://
openweathermap.org/api.