plugins {
id("com.android.application")
id("org.jetbrains.kotlin.android")
}

android {
namespace = "com.omniscan.xr"
compileSdk = 35

defaultConfig {
applicationId = "com.omniscan.xr"
minSdk = 28
targetSdk = 35
versionCode = 1
versionName = "1.0.0-PRO"
}

buildFeatures {
compose = true
}

composeOptions {
kotlinCompilerExtensionVersion = "1.5.1"
}
}

dependencies {
implementation("com.google.ar:core:1.42.0")
implementation("androidx.activity:activity-compose:1.8.2")
implementation(platform("androidx.compose:compose-bom:2023.10.01"))
implementation("androidx.compose.ui:ui")
implementation("androidx.compose.material3:material3")
implementation("com.squareup.retrofit2:retrofit:2.9.0")
implementation("com.squareup.retrofit2:converter-gson:2.9.0")
implementation("org.jetbrains.kotlinx:kotlinx-coroutines-android:1.7.3")
}
