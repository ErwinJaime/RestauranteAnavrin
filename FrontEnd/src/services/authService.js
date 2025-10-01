// Servicio de autenticación para manejar JWT y operaciones de usuario
import axios from "axios";

// Cambiar la línea 4:
const API_BASE_URL = process.env.VUE_APP_API_BASE_URL || "http://127.0.0.1:8000/api/usuarios";

class AuthService {
  constructor() {
    this.token = localStorage.getItem("access_token");
    this.refreshToken = localStorage.getItem("refresh_token");
    this.user = JSON.parse(localStorage.getItem("user") || "null");

    // Crear instancia de axios con configuración base
    this.axiosInstance = axios.create({
      baseURL: API_BASE_URL,
      headers: {
        "Content-Type": "application/json",
      },
    });
  }

  // Método para hacer login
  async login(email, password) {
    try {
      const response = await this.axiosInstance.post("/login/", {
        correo: email,
        password: password,
      });

      const data = response.data;

      this.setTokens(data.access, data.refresh);
      this.setUser(data.usuario);

      return { success: true, user: data.usuario };
    } catch (error) {
      console.error("Error en login:", error);
      return {
        success: false,
        error: error.response?.data?.error || "Credenciales incorrectas",
      };
    }
  }

  // Método para registrar usuario
  async register(userData) {
    try {
      const response = await this.axiosInstance.post("/registro/", userData);
      const data = response.data;

      return { success: true, message: data.mensaje };
    } catch (error) {
      console.error("Error en registro:", error);
      return {
        success: false,
        error: error.response?.data?.error || "Error al registrar usuario",
      };
    }
  }

  // Método para hacer logout
  logout() {
    localStorage.removeItem("access_token");
    localStorage.removeItem("refresh_token");
    localStorage.removeItem("user");
    this.token = null;
    this.refreshToken = null;
    this.user = null;
  }

  // Verificar si el usuario está autenticado
  isAuthenticated() {
    return !!this.token && !!this.user;
  }

  // Obtener token
  getToken() {
    return this.token;
  }

  // Obtener datos del usuario
  getUser() {
    return this.user;
  }

  // Guardar tokens
  setTokens(accessToken, refreshToken) {
    this.token = accessToken;
    this.refreshToken = refreshToken;
    localStorage.setItem("access_token", accessToken);
    localStorage.setItem("refresh_token", refreshToken);

    // actualizar headers del axiosInstance
    this.axiosInstance.defaults.headers["Authorization"] = `Bearer ${accessToken}`;
  }

  // Guardar usuario
  setUser(user) {
    this.user = user;
    localStorage.setItem("user", JSON.stringify(user));
  }

  // Refrescar token
  async refreshAccessToken() {
    if (!this.refreshToken) return false;

    try {
      const response = await this.axiosInstance.post("/refresh/", {
        refresh: this.refreshToken,
      });

      const data = response.data;
      this.setTokens(data.access, this.refreshToken);
      return true;
    } catch (error) {
      console.error("Error al refrescar token:", error);
      this.logout();
      return false;
    }
  }

  // Hacer peticiones autenticadas
  async authenticatedRequest(url, options = {}) {
    if (!this.token) throw new Error("No hay token de acceso");

    try {
      const response = await this.axiosInstance.request({
        url,
        ...options,
        headers: {
          Authorization: `Bearer ${this.token}`,
          ...(options.headers || {}),
        },
      });

      return response;
    } catch (error) {
      if (error.response?.status === 401) {
        const refreshed = await this.refreshAccessToken();
        if (refreshed) {
          return this.axiosInstance.request({
            url,
            ...options,
            headers: {
              Authorization: `Bearer ${this.token}`,
              ...(options.headers || {}),
            },
          });
        } else {
          throw new Error("Sesión expirada");
        }
      }
      throw error;
    }
  }
}

// Crear una instancia única del servicio
const authService = new AuthService();

export default authService;
