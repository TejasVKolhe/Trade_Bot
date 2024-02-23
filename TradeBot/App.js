import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import SigninScreen from './src/screens/SigninScreen';
import SignInScreen from './src/screens/SigninScreen/SignInScreen';

const  App = () => {
  return (
    <View style={styles.root}>
      <SigninScreen/>
    </View>
  );
}

const styles = StyleSheet.create({
  root: {
    flex: 1,
    backgroundColor: 'silver',
  },
});



export default App;