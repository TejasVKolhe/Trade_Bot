import {
  View,
  Text,
  Image,
  StyleSheet,
  useWindowDimensions,
} from "react-native";
import React from "react";
import Logo from "../../../assets/images/Logo.jpg";

const SignInScreen = () => {
  const { height } = useWindowDimensions();
  return (
    <View style={styles.root}>
      <Image source={Logo} style={[styles.logo, { height: height * 0.5 }]} />
      <Text></Text>
    </View>
  );
};

const styles = StyleSheet.create({
  root: {
    alignItems: "center",
    padding: 20,
  },
  logo: {
    borderRadius : 10,
    marginTop: 50,
    width: "80%",
    maxWidth: 300,
    maxHeight: 200,
  },
});

export default SignInScreen;
