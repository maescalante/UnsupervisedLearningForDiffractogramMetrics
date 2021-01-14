import numpy as np
from scipy import linalg
from numpy.linalg import norm


class SNE_RAW():

    def __init__(self, components=2, v=1, iterations=1000, lr=0.01):
        """"
        t-sne constructor
        """
        self.MACHINE_EPSILON = np.finfo(np.double).eps
        self.n_components = components
        self.v = v
        self.iterations = iterations
        self.lr = lr
        self.n_samples = 0

    def probabilities(self, metrics):
        """"
        Compute the probabilities matrix.
        """
        metrics = metrics.astype(np.float32, copy=False)

        P = np.zeros((self.n_samples, self.n_samples), dtype=np.float64)

        sum_pi = 0
        for i in range(self.n_samples):
            for j in range(self.n_samples):
                if i == j:
                    P[i, j] = 0.0
                else:
                    P[i, j] = -np.power(metrics[i, j], 2)
                    sum_pi += P[i, j]

            P /= (2 * np.power(self.v, 2))
            sum_pi /= (2 * np.power(self.v, 2))
        P = np.maximum(P / sum_pi, self.MACHINE_EPSILON)
        return P

    def fit(self, X):
        """"
        Performs t-sne
        """
        self.n_samples = X.shape[0]
        P = self.probabilities(metrics=X)
        X_embedded = 1e-4 * np.random.randn(self.n_samples, self.n_components).astype(np.float32)

        return self._tsne(P, X_embedded=X_embedded)

    def _dist(self, X):
        ans = np.zeros((self.n_samples, self.n_samples), dtype=np.float64)
        for i in range(self.n_samples):
            for j in range(self.n_samples):
                ans[i, j] = norm(X[i, :] - X[j, :])
        return ans

    def _tsne(self, P, X_embedded):
        params = X_embedded.ravel()

        obj_func = self._kl_divergence

        params = self._gradient_descent(obj_func, params, [P])

        X_embedded = params.reshape(self.n_samples, self.n_components)
        return X_embedded

    def _kl_divergence(self, params, P):
        X_embedded = params.reshape(self.n_samples, self.n_components)

        dist = -self._dist(X_embedded)
        Q = np.maximum(np.exp(dist / np.sum(dist)), self.MACHINE_EPSILON)

        # Kullback-Leibler divergence of P and Q
        print(P.shape, Q.shape, X_embedded.shape, dist.shape)
        kl_divergence = np.sum(np.sum(np.dot(P, np.log(np.maximum(P, self.MACHINE_EPSILON) / Q))))

        # Gradient: dC/dY
        grad = np.ndarray((self.n_samples, self.n_components), dtype=params.dtype)
        # PQd = squareform((P - Q) * dist) # MK NO SE COMO CALCULAR EL MK GRADIENTE !!!
        for i in range(self.n_samples):
            g = 0
            for j in range(self.n_samples):
                g += (P[j, i] - Q[j, i] + P[i, j] - Q[i, j]) * (X_embedded[i, :] - X_embedded[j, :])
            grad[i] = g
        grad = 2 * grad.ravel()
        return kl_divergence, grad

    def _gradient_descent(self, obj_func, p0, args, it=0, n_iter=1000,
                          n_iter_check=1, n_iter_without_progress=300,
                          momentum=0.8, learning_rate=200.0, min_gain=0.01,
                          min_grad_norm=1e-7):

        p = p0.copy().ravel()
        update = np.zeros_like(p)
        gains = np.ones_like(p)
        error = np.finfo(np.float).max
        best_error = np.finfo(np.float).max
        best_iter = i = it

        for i in range(it, n_iter):
            error, grad = obj_func(p, *args)
            grad_norm = linalg.norm(grad)
            inc = update * grad < 0.0
            dec = np.invert(inc)
            gains[inc] += 0.2
            gains[dec] *= 0.8
            np.clip(gains, min_gain, np.inf, out=gains)
            grad *= gains
            update = momentum * update - learning_rate * grad
            p += update
            print(error)
            print("[t-SNE] Iteration %d: error = %.7f,"
                  " gradient norm = %.7f"
                  % (i + 1, error, grad_norm))

            if error < best_error:
                best_error = error
                best_iter = i
            elif i - best_iter > n_iter_without_progress:
                break

            if grad_norm <= min_grad_norm:
                break
        return p
